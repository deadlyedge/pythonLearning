from prettytable import PrettyTable
table = PrettyTable(['No.', 'CVI', 'VUL', 'Rule', 'Lang', 'Level-Score', 'Target', 'Commit(Time, Author)', 'Source Code Content', 'Analysis'])
table.align = 'l'
trigger_rules = []
row = ["1", "130001", "HCP", "password", "PHP", "L-02: ■■□□□□□□□□", "config.php:32", "Unknown, @Unknown", "$dbpassword = 'root';", "REGEX-ONLY-MATCH"]
table.add_row(row)
print(table)