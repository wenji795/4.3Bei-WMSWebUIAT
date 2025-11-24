# driver相关配置项
#浏览器类型：chrome/edge
BROWSER_TYPE = "chrome"

#使用哪种浏览器驱动管理方式：local/其他
DRIVER_TYPE = "local"

#本地浏览器驱动路径
CHROME_DRIVER_PATH = "./driver/chromedriver"
EDGE_DRIVER_PATH = "./driver/"

#是否开启无头模式
HEADLESS = False

# excel格式的测试用例文件配置
EXCEL_FILE = "./data/3.7_6.xlsx"
EXCEL_SHEET_NAME = "Sheet1"

# wms的mysql配置
DB_HOST = "60.204.225.104"
DB_PORT = 3306
DB_NAME = "wms"
DB_USER = "student_xiaobei"
DB_PASSWORD = "xiaobeiup"
