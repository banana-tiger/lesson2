import ephem

def main():

    def receive_full_moon_date(user_text):
        trash_list = [",", ".", "\\", "-"]
        splitted_user_text = user_text.split()[1]
        for word in splitted_user_text:
            for symbol in word:
                if symbol in trash_list:
                    splitted_user_text = splitted_user_text.replace(symbol, "/")
                else:
                    break
        splitted_date = splitted_user_text.split("/")

        for index, number in enumerate(splitted_date):
            if len(number) > 3:
                year = splitted_date.pop(index)
                if index == 0:
                    month = splitted_date.pop(index + 1)
                    day = splitted_date.pop()
                elif index == 2:
                    month = splitted_date.pop(index - 1)
                    day = splitted_date.pop(index - 2)
            else:
                continue

        correct_date = "/".join([year, month, day])
        return correct_date
    print(receive_full_moon_date("/command 23-02-1999"))


if __name__ == "__main__":
    main()