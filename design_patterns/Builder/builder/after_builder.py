from director import Director
from builders import MyComputerBuilder, BudgetBoxBuilder

if __name__ == '__main__':
    computer_builder = Director(MyComputerBuilder())
    computer_builder.build_computer()
    computer = computer_builder.get_computer()
    computer.display()

    print()

    computer_builder = Director(BudgetBoxBuilder())
    computer_builder.build_computer()
    computer = computer_builder.get_computer()
    computer.display()
