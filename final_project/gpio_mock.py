class GPIO:
    BCM = 'BCM'
    OUT = 'OUT'
    IN = 'IN'
    HIGH = 1
    LOW = 0

    @staticmethod
    def setmode(mode):
        print(f"[MOCK GPIO] setmode({mode})")

    @staticmethod
    def setup(pin, mode):
        print(f"[MOCK GPIO] setup(pin={pin}, mode={mode})")

    @staticmethod
    def output(pin, state):
        state_str = 'HIGH' if state == GPIO.HIGH else 'LOW'
        print(f"[MOCK GPIO] output(pin={pin}, state={state_str})")

    @staticmethod
    def input(pin):
        value = GPIO.HIGH  # or random choice if simulating
        print(f"[MOCK GPIO] input(pin={pin}) → {value}")
        return value

    @staticmethod
    def cleanup():
        print("[MOCK GPIO] cleanup()")
