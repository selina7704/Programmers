def solution(hp):
    general = hp // 5
    remaining = hp % 5
    soldier = remaining // 3
    worker = remaining % 3
    return general + soldier + worker