print("hello")


class Voice:
    voice_dictionary = {
        "Cat": "meow",
        "Dog": "bark",
        "Human": "hello"
    }

    def __init__(self, kind, state):
        self._kind = kind
        self._state = state

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, value):
        if value in self.voice_dictionary.keys():
            self._kind = value
        else:
            raise ValueError("not a valid kind enter str")

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        state_options = ["good", "ok", "bad"]
        if value in state_options:
            self._state = value
        else:
            raise ValueError("not a valid state, choose from list in enum")

    def make_noise(self):
        print(self.voice_dictionary[self._kind])

    def speak_to(self, kind):
        msg = ""
        if self._state == "good":
            msg = "your voice is so beautiful"
        elif self._state == "ok":
            msg = "you sound like usual"
        elif self._state == "bad":
            msg = "you sound awful. go see a doctor"

        other_name = kind._kind
        this_name = self._kind
        print("{} i'm a {}\nhello {}, {}\n{}".format(self.voice_dictionary[other_name], other_name, this_name, msg,
                                                     self.voice_dictionary[other_name]))
