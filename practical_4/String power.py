# String power

def string_power(k, a_str):
    if k >= 0:
        return a_str * k
    else:
        str_len = len(a_str)
        step = abs(str_len / k)
        div_perf = step.is_integer()
        if div_perf:
            step = int(step)
            part = a_str[:step]

            for i in range(step, str_len, step):
                if a_str[i:i + step] != part:
                    return "undefined"
            else:
                return part
        else:
            return "undefined"


if __name__ == "__main__":
    a_string = input()
    an_integer = int(input())
    print(string_power(an_integer, a_string))