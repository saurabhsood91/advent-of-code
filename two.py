import sys

# opcodes
ADD = 1
MULTIPLY = 2
HALT = 99

def opcode_computer(data):
  input = [x for x in data]
  current_position = 0
  while input[current_position] != HALT:
    opcode = input[current_position]
    first_operand = input[input[current_position + 1]]
    second_operand = input[input[current_position + 2]]
    output_position = input[current_position + 3]
    if opcode == ADD:
      input[output_position] = first_operand + second_operand
    elif opcode == MULTIPLY:
      input[output_position] = first_operand * second_operand
    else:
      # Need to take a long hard look in the mirror
      sys.exit(-1)
    # advance by four steps
    current_position += 4
  return input[0]


def gravity_assist_computer(data):
  for noun in range(0, 100):
    for verb in range(0, 100):
      input = [x for x in data]
      input[1] = noun
      input[2] = verb
      if opcode_computer(input) == 19690720:
        return (noun, verb)

if __name__ == '__main__':
  input = list(map(int, open('two.txt').read().split(',')))

  # gravity assist program state
  input[1] = 41
  input[2] = 12

  # print(opcode_computer(input))
  noun, verb = gravity_assist_computer(input)
  print(100 * noun + verb)

  # assert opcode_computer(input) == 19690720

  # assert opcode_computer([1,1,1,4,99,5,6,0,99]) == 30
  # assert opcode_computer([2,4,4,5,99,0]) == 2
  # assert opcode_computer([1,9,10,3,2,3,11,0,99,30,40,50]) == 3500




      