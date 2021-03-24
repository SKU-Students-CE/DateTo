from datetime import date as dt
from persiantools.jdatetime import JalaliDate
from pyperclip import copy


class DateTo:
    def __init__(self):
        list_dates = {"کوییز 1 ریاضی 2 رئیسی": [(1400, 1, 21)],
                      "میان ترم زبان تخصصی گروه 1": [(1400, 1, 28)],
                      "میان ترم ریاضیات گسسته": [(1400, 1, 29)],
                      "میان ترم زبان تخصصی گروه 2": [(1400, 1, 31)],
                      "میان ترم ریاضی 2 رئیسی": [(1400, 2, 19)],
                      "کوییز 2 ریاضی 2 رئیسی": [(1400, 3, 8)],
                      "پایان ترم ریاضیات گسسته": [(1400, 3, 24), "8:30-10:30"],
                      "پایان ترم فارسی عمومی": [(1400, 3, 25), "15:30-17:30"],
                      "پایان ترم ریاضی 2": [(1400, 3, 29), "10:30-12:30"],
                      "پایان ترم معادلات دیفرانسیل": [(1400, 4, 2), "10:30-12:30"],
                      "پایان ترم انقلاب اسلامی": [(1400, 4, 3), "13:30-15:30"],
                      "پایان ترم تفسیر موضوعی": [(1400, 4, 3), "8:30-10:30"],
                      "پایان ترم تاریخ اسلام": [(1400, 4, 3), "10:30-12:30"],
                      "پایان ترم مبانی کامپیوتر": [(1400, 4, 5), "8:30-10:30"],
                      "پایان ترم فیزیک 2": [(1400, 4, 7), "13:30-15:30"],
                      "پایان ترم زبان تخصصی": [(1400, 4, 9), "8:30-10:30"],
                      "پایان ترم تربیت بدنی": [(1400, 4, 10), "10:30-12:30"],
                      }

        list_date = {k: v for k, v in sorted(list_dates.items(), key=lambda item: item[1][0])}

        self.keeper = []

        for item in list_date.items():
            self.calculator(item)

        today_date = str(JalaliDate.today()).split("-")
        to_print = "#تاریخ_امتحانات\n#تاریخ\n#امتحانات\n\n" + \
                   "امروز : {}/{}/{}".format(today_date[0], today_date[1], today_date[2]) + \
                   "\n\n" + "\n\n".join(self.keeper) + "\n\n" + \
                   "🤓 اعداد زیر هر تاریخ فاصله امروز تا روز امتحانه 🤓" + \
                   "\n\n================"

        copy(to_print)
        print(to_print)

    def calculator(self, item):
        date_name = item[0]
        date = item[1][0]
        date_str = "{}/{}/{}".format(date[0], date[1], date[2])

        target_date = JalaliDate(date[0], date[1], date[2]).to_gregorian()
        today_date = dt.today()
        days_left = target_date - today_date

        if len(item[1]) > 1:
            self.keeper.append("{0}:\n{1} ==> {2}\n{3}".format(date_name, date_str, item[1][1], days_left.days))
        else:
            self.keeper.append("{0}:\n{1}\n{2}".format(date_name, date_str, days_left.days))


if __name__ == "__main__":
    DateTo()

# print(JalaliDate.to_jalali(2021, 3, 23))
