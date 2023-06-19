class Counter:
    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        self.current = start

    def set_max(self, max_max):
        self.max_value = max_max

    def set_min(self, min_min):
        self.min_value = min_min

    def step_up(self):
        if self.current < self.max_value:
            self.current += 1
        else:
            raise ValueError("Достигнут максимум")

    def step_down(self):
        if self.current > self.min_value:
            self.current -= 1
        else:
            raise ValueError("Достигнут минимум")

    def get_current(self):
        return self.current


# Приклад
counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10
try:
    counter.step_up()
except ValueError as e:
    print(e)
assert counter.get_current() == 10

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7
try:
    counter.step_down() 
except ValueError as e:
    print(e)
assert counter.get_current() == 7