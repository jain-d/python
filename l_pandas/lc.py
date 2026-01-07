import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    email_set: set = set()
    repeated_emails = set()

    for email in person["email"]:
        if email not in email_set:
            email_set.add(email)
        else:
            repeated_emails.add(email)
    return pd.DataFrame(repeated_emails, columns=pd.Index(["Email"]))


test_df = pd.DataFrame()
test_df["id"] = [1, 2, 3]
test_df["email"] = ["a@b.com", "c@d.com", "a@b.com"]
test_df["email"] = test_df["email"].astype("string")

received_df = duplicate_emails(test_df)

print(received_df)



# 183ms
def duplicate_emails1(person: pd.DataFrame) -> pd.DataFrame:
    email_counts = person.groupby("email").size().reset_index(name='count')
    duplicated_emails = email_counts[email_counts['count']>1][['email']]
    return duplicated_emails

# 153ms
def duplicate_emails2(person: pd.DataFrame) -> pd.DataFrame:
    return person.loc[person.duplicated(['email']),['email']].drop_duplicates()

# 107ms
def duplicate_emails3(person: pd.DataFrame) -> pd.DataFrame:
    return person[person['email'].duplicated()][['email']].rename(columns={'email': 'Email'}).drop_duplicates()
