"""
Иногда возникает необходимость перенаправить вывод в нужное нам место внутри программы по ходу её выполнения.
Реализуйте контекстный менеджер, который принимает два IO-объекта (например, открытые файлы)
и перенаправляет туда стандартные потоки stdout и stderr.

Аргументы контекстного менеджера должны быть непозиционными,
чтобы можно было ещё перенаправить только stdout или только stderr.
"""

import sys, types, traceback
from typing import IO, Type, Literal


class Redirect:
    def __init__(self, stdout: IO = None, stderr: IO = None) -> None:
        self.stdout = stdout
        self.stderr = stderr
        self._stdout_backup = None
        self._stderr_backup = None

    def __enter__(self):
        self._stdout_backup = sys.stdout
        self._stderr_backup = sys.stderr
        if self.stdout:
            sys.stdout = self.stdout
        if self.stderr:
            sys.stderr = self.stderr
        return self

    def __exit__(
            self,
            exc_type: Type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: types.TracebackType | None
    ) -> None:
        sys.stdout = self._stdout_backup
        sys.stderr = self._stderr_backup
        if exc_val is not None and self.stderr:
            traceback.print_exception(exc_type, exc_val, exc_tb, file=self.stderr)
