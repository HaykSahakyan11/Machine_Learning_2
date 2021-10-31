# unique-email-addresses

def numUniqueEmails(emails):

    def convert(email):
        name, domain = email.split('@')
        name_, *_ = name.split('+')
        return "".join(["".join(name_.split(".")), '@', domain])

    lookup = set()
    for email in emails:
        lookup.add(convert(email))
    return len(lookup)


emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
emails_2 = ["test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com"]

print(numUniqueEmails(emails))
