class Vacancies:
    def __init__(self, title, url, payment_from, payment_to, description, platform=""):
        self.title = title  #
        self.url = url
        self.payment_from = payment_from
        self.payment_to = payment_to
        self.description = description
        self.platform = platform  #hh или sj

    def __str__(self):
        title = ""
        description = ""
        url = ""
        payment = ""

        if self.title:
            title = f"{self.title}\n"
        if self.description:
            description = f"{self.description}\n"
        if self.payment_to == 0 and self.payment_from == 0:
            payment = "Оплата не указана\n"
        else:
            if self.payment_from > 0:
                payment = f"от {self.payment_from} "
            if self.payment_to > 0:
                payment += f"до {self.payment_to}"
            payment += " руб.\n"
        if self.url:
            url = f"адрес: {self.url}"
        vac_str = f"\n{title}{description}{payment}{url}\n---"
        return vac_str
