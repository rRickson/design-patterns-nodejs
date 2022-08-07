
class Target:

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adapter:

    def specific_request(self) -> str:
        return "9876543210"


class Adapter(Target, Adapter):
  
    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {sorted(self.specific_request())}"


def client_code(target: "Target") -> None:
    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)


# Since all will be used JSON as main conversation data there is no need to a adapter to it.
# Use the Adapter class when you want to use some existing class, but its interface isn’t compatible with the rest of your code.