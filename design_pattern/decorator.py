""" Decorator Pattern
"""
from abc import ABC, abstractmethod
from typing import final, Union


class Display(ABC):
    @abstractmethod
    def get_columns(self) -> int:
        pass

    @abstractmethod
    def get_rows(self) -> int:
        pass

    @abstractmethod
    def get_row_text(self, row: int) -> Union[None, str]:
        pass

    @final
    def show(self) -> None:
        for i in range(self.get_rows()):
            print(self.get_row_text(i))


class StringDisplay(Display):
    def __init__(self, string: str):
        """ string must not include \n
        """
        self.string = string

    def get_columns(self) -> int:
        return len(self.string)

    def get_rows(self) -> int:
        # ignore \n
        return 1

    def get_row_text(self, row: int) -> Union[None, str]:
        if row == 0:
            return self.string
        else:
            return None


class Boader(Display):
    def __init__(self, display: Display):
        self.display = display


class SideBoader(Boader):
    def __init__(self, display: Display, char: str):
        super().__init__(display)
        self.boader_char = char

    def get_columns(self) -> int:
        """ Get length that is sum of boarder length at both side and containt.
        """
        boader_len = len(self.boader_char)
        return boader_len * 2 + self.display.get_columns()

    def get_rows(self) -> int:
        return self.display.get_rows()

    def get_row_text(self, row: int) -> Union[None, str]:
        return (
            f"{self.boader_char}"
            f"{self.display.get_row_text(row)}"
            f"{self.boader_char}"
        )


class FullBoader(Boader):
    def __init__(self, display: Display):
        super().__init__(display)

    def get_columns(self) -> int:
        """ Get length that is sum of boarder length at both side and containt.
        """
        return 1 + self.display.get_columns() + 1

    def get_rows(self) -> int:
        """ Get rows that is sum of contants and top and bottom boader.
        """
        return 1 + self.display.get_rows() + 1

    def get_row_text(self, row: int) -> Union[None, str]:
        if row == 0:
            return f"+{self.make_line('-', self.display.get_columns())}+"
        elif row == self.display.get_rows() + 1:
            return f"+{self.make_line('-', self.display.get_columns())}+"
        else:
            return f"|{self.display.get_row_text(row - 1)}|"

    def make_line(self, char: str, count: int):
        """ Make the string by concatenating 10 characters
        """
        return char * count


if __name__ == "__main__":
    b1 = StringDisplay("Hello World")
    b2 = SideBoader(b1, "#")
    b3 = FullBoader(b2)
    b1.show()
    b2.show()
    b3.show()

    b4 = SideBoader(
        FullBoader(
            FullBoader(
                FullBoader(
                    SideBoader(
                        FullBoader(
                            StringDisplay("Hello!")
                        ),
                        "*"
                    )
                )
            )
        ),
        "#"
    )
    b4.show()
