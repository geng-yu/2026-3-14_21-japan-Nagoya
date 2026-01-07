import matplotlib.pyplot as plt
from datetime import date
import matplotlib.font_manager as fm
import platform

# ==========================================
# 1. 字型設定 (防止中文亂碼)
# ==========================================
def set_chinese_font():
    system = platform.system()
    if system == "Windows":
        font_path = 'C:\\Windows\\Fonts\\msjh.ttc' # 微軟正黑體
    elif system == "Darwin": # Mac
        font_path = '/System/Library/Fonts/STHeiti Light.ttc'
    else:
        font_path = None # Linux 需自行指定

    if font_path:
        prop = fm.FontProperties(fname=font_path)
        plt.rcParams['font.family'] = prop.get_name()
    else:
        plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'SimHei'] 
    
    plt.rcParams['axes.unicode_minus'] = False

# ==========================================
# 2. 行程詳細內容 (Day Lists)
#    (這裡先幫你填入大概的景點，可自行修改)
# ==========================================
day1 = ["桃園機場 TPE", "小松機場 KMQ", "租車 / 移動", "金澤飯店 Check-in", "晚餐：金澤車站"]
day2 = ["近江町市場 (早午餐)", "金澤城公園", "兼六園 (雪吊)", "東茶屋街 (下午茶)", "晚餐：香林坊/片町"]
day3 = ["移動前往合掌村", "合掌村散策", "展望台", "移動前往高山", "高山老街 (上三之町)", "晚餐：飛驒牛燒肉"]
day4 = ["宮川朝市", "新穗高纜車", "平湯溫泉 (路過)", "高山陣屋", "返回高山飯店"]
day5 = ["移動前往牧歌之里", "牧歌之里 (玩雪)", "移動前往犬山", "犬山城 & 城下町", "移動前往名古屋"]
day6 = ["名古屋榮商圈", "綠洲21", "電視塔", "百貨公司購物", "晚餐：蓬萊軒鰻魚飯"]
day7 = ["大須觀音", "大須商店街", "名古屋城", "熱田神宮", "世界的山將 (手羽先)"]
day8 = ["早餐 / 整理行李", "中部國際機場 NGO", "免稅店採購", "搭機返台", "溫暖的家"]

# ==========================================
# 3. 主要資料結構 (你的修改需求)
#    Key 前後加了空格以撐開欄寬，維持兩行顯示
# ==========================================
trip_dates = {
    "  Day 1  \n1/17(六)": (date(2026, 1, 17), day1, "Day 1: 出發 & 移動"),
    "  Day 2  \n1/18(日)": (date(2026, 1, 18), day2, "Day 2: 金澤市區"),
    "  Day 3  \n1/19(一)": (date(2026, 1, 19), day3, "Day 3: 合掌村 & 飛驒"),
    "  Day 4  \n1/20(二)": (date(2026, 1, 20), day4, "Day 4: 新穗高 & 高山"),
    "  Day 5  \n1/21(三)": (date(2026, 1, 21), day5, "Day 5: 牧歌 & 犬山"),
    "  Day 6  \n1/22(四)": (date(2026, 1, 22), day6, "Day 6: 名古屋榮商圈"),
    "  Day 7  \n1/23(五)": (date(2026, 1, 23), day7, "Day 7: 大須 & 名古屋城"),
    "  Day 8  \n1/24(六)": (date(2026, 1, 24), day8, "Day 8: 回程"),
}

# ==========================================
# 4. 繪圖邏輯
# ==========================================
def create_schedule_image():
    set_chinese_font()
    
    # 準備表格資料
    columns = list(trip_dates.keys())
    
    # 找出最長的行程清單長度，補齊空字串以免表格報錯
    max_len = max(len(data[1]) for data in trip_dates.values())
    cell_text = []
    
    for i in range(max_len):
        row = []
        for k in columns:
            items = trip_dates[k][1] # 取得 dayX list
            if i < len(items):
                row.append(items[i])
            else:
                row.append("") # 補空
        cell_text.append(row)

    # 設定畫布大小 (寬一點，讓文字好伸展)
    fig, ax = plt.subplots(figsize=(20, 10)) 
    ax.set_axis_off()
    
    # 建立表格
    # colWidths 設定為 0.12 (適度加寬，避免換行)
    table = ax.table(
        cellText=cell_text,
        colLabels=columns,
        cellLoc='center',
        loc='center',
        colWidths=[0.12] * len(columns) 
    )
    
    # 美化表格樣式
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 2) # 拉高單格高度 (Scale height)

    # 針對 Header 做特殊設定 (粗體、顏色)
    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_text_props(weight='bold', color='white')
            cell.set_facecolor('#40466e') # 深藍色 Header
            cell.set_edgecolor('white')
        else:
            # 奇偶數行變色 (斑馬紋)
            if row % 2 == 0:
                cell.set_facecolor('#f2f2f2')
            else:
                cell.set_facecolor('white')

    # 加入主標題
    plt.title("2026 日本北陸之旅 (1/17 - 1/24)", fontsize=18, weight='bold', pad=20)
    
    # 顯示並儲存
    plt.tight_layout()
    plt.savefig('japan_trip_schedule.png', dpi=300, bbox_inches='tight')
    print("行程表已生成：japan_trip_schedule.png")
    plt.show()

if __name__ == "__main__":
    create_schedule_image()
