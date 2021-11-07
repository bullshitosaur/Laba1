from Pieces import Pawn, King, Queen, Bishop, Knight, Rook


req = 'idle'
board_x = 8
board_y = 8
piece_names = {'pawn': Pawn(), 'king': King(), 'queen': Queen(),
               'bishop': Bishop(), 'knight': Knight(), 'rook': Rook()}


inp = open('input.txt', 'r')
out = open('output.txt', 'w')

for req in inp:
    req = req.lower().strip(' \n')
    if req == '':
        continue
    req_base = req.split(':')[0].strip(' ')
    if req_base == 'board':
        board_x = int(req.split(':')[1].split('-')[0].strip(' '))
        board_y = int(req.split(':')[1].split('-')[1].strip(' '))
        out.write(f'Board changed to {board_x}x{board_y}.\n')
    elif req_base in piece_names:
        points = req.split(':')[1].strip(' ').split(';')
        final_output = f'{piece_names[req_base].name}: '
        for point in points:
            if point.strip(' \n') == '':
                continue
            possible_moves = piece_names[req_base].possible_moves(board_x,
                                                                  board_y,
                                                                  int(point.split('-')[0].strip(' ')),
                                                                  int(point.split('-')[1].strip(' ')))
            final_output += f'{possible_moves}; '
        out.write(f'{final_output[:len(final_output) - 2]}.\n')
    else:
        out.write('Bad request\n')

inp.close()
out.close()