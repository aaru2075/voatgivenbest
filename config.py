env_vars = {
  # Get From my.telegram.org
  "API_HASH": "a1bcb2e0191095a0758e29280cf55933",
  # Get From my.telegram.org
  "API_ID": "23678651",
  #Get For @BotFather
  "BOT_TOKEN": "8049998303:AAHy2_GdJFep9wqhTzd_exDZ_lqY_YbxqUQ",
  # Get For tembo.io
  "DATABASE_URL_PRIMARY": "postgresql://postgres:rhf04OpB0SbaE2Yw@inversely-immaculate-oryx.data-1.use1.tembo.io:5432/postgres",
  # Logs Channel Username Without @
  "CACHE_CHANNEL": "",
  # Force Subs Channel username without @
  "CHANNEL": "",
  # {chap_num}: Chapter Number
  # {chap_name} : Manga Name
  # Ex : Chapter {chap_num} {chap_name} @Manhwa_Arena
  "FNAME": "[MC] [{chap_num}] {chap_name} @Manga_Campus"
}

dbname = env_vars.get('DATABASE_URL_PRIMARY') or env_vars.get('DATABASE_URL') or 'sqlite:///test.db'

if dbname.startswith('postgres://'):
    dbname = dbname.replace('postgres://', 'postgresql://', 1)
    
