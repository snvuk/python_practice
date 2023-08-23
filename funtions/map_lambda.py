df1 = "Df 1: "
df2 = "Df 2: "
df3 = "Df 3: "
list_of_df = [df1, df2, df3]

add_date = lambda df: df + "Date: 2023-08-22"

mod_list = list(map(add_date, list_of_df))

for mod_df in mod_list:
    print(mod_df)
