import sys

sys.stdout.write(
    "\n".join(
        map(
            str,
            [
                (lambda x, y: x + y)(
                    *map(int, sys.stdin.readline().strip().split())
                )
                for i in range(int(sys.stdin.readline().strip()))
            ]
        )
    )
    + "\n"
)
