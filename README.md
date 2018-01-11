# NYUST_PTT_Crawler

如果在windows 使用第三方terminal(例如:git bash)操作時 print()中文時，可能會出現
UnicodeEncodeError: 'cp950' codec can't encode character
這是因為即便說你是用utf-8格式 但是windows 會強制用cp950在轉一次
如果把輸出改成這樣
print(res.encode("utf8").decode("cp950", "ignore"))
雖然會過 但是中文顯示會亂碼

所以使用windows環境時 還請用正規的cmd 或是powershell
