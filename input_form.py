import tkinter as tk
from tkinter import ttk

# アプリケーションのメインウィンドウを作成
root = tk.Tk()
root.title("入力画面")

# ラベルとエントリー（テキストボックス）を作成する関数
def create_label_entry(parent, label_text, row, column, columnspan=1, **options):
    label = tk.Label(parent, text=label_text)
    label.grid(row=row, column=column, sticky="e")
    entry = tk.Entry(parent, **options)
    entry.grid(row=row, column=column+1, columnspan=columnspan, sticky="ew")
    return entry

# ラベルとプルダウンメニューを作成する関数
def create_label_dropdown(parent, label_text, options, row, column, columnspan=1):
    label = tk.Label(parent, text=label_text)
    label.grid(row=row, column=column, sticky="e")
    variable = tk.StringVar(parent)
    variable.set(options[0])  # デフォルト値を設定
    dropdown = ttk.Combobox(parent, textvariable=variable, values=options, state='readonly')
    dropdown.grid(row=row, column=column+1, columnspan=columnspan, sticky="ew")
    return dropdown


# 要員名のウィジェットを動的に生成する関数
staff_entries = []

def update_staff_entries():
    # 既存のウィジェットを削除する
    for entry in staff_entries:
        entry[0].destroy()
        entry[1].destroy()
    staff_entries.clear()

    # 新しい要員人数の値に基づいて要員名のウィジェットを生成する
    try:
        staff_count = int(staff_number_entry.get())
    except ValueError:
        # 入力が無効な場合は何もしない
        staff_count = 0

    current_row = 1  # 要員人数エントリーの下の行
    for i in range(staff_count):
        current_row += 1
        staff_label = tk.Label(contract_info_frame, text=f"要員名 {i+1}")
        staff_label.grid(row=current_row, column=0, sticky="e")
        staff_entry = tk.Entry(contract_info_frame)
        staff_entry.grid(row=current_row, column=1, sticky="ew")
        staff_entries.append((staff_label, staff_entry))

    # 要員名のエントリーの後にフレームを配置する
    next_row = current_row + 1
    contract_price_frame.grid(row=next_row, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
    working_hours_frame.grid(row=next_row + 1, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
    cost_info_frame.grid(row=next_row + 2, column=0, columnspan=2, sticky="ew", padx=10, pady=5)


# 基本データ #################################################################################
# 基本データのフレーム
basic_data_frame = tk.LabelFrame(root, text="▶基本データ")
basic_data_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

# 文書番号
doc_number_entry               = create_label_entry(basic_data_frame, "文書番号", 0, 0)

# 以下、実際には各種プルダウンメニューのオプションを設定する必要があります
customer_name_dropdown         = create_label_dropdown(basic_data_frame, "顧客名", ["", "顧客A", "顧客B"], 1, 0)
project_name_dropdown          = create_label_dropdown(basic_data_frame, "案件名", ["", "案件X", "案件Y"], 2, 0)
start_month_dropdown           = create_label_dropdown(basic_data_frame, "開発開始月", ["", "1月", "2月"], 3, 0)
end_month_dropdown             = create_label_dropdown(basic_data_frame, "開発終了月", ["", "3月", "4月"], 4, 0)
estimation_department_dropdown = create_label_dropdown(basic_data_frame, "見積算定部門", ["", "部門1", "部門2"], 5, 0)

# 見積算定者
estimator_entry                = create_label_entry(basic_data_frame, "見積算定者", 6, 0)
############################################################################################

# 請負契約基本情報データ #####################################################################
# 請負契約基本情報のフレーム
contract_info_frame = tk.LabelFrame(root, text="▶請負契約基本情報")
contract_info_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
contract_info_frame.columnconfigure(1, weight=1) # エントリーが拡張されるように設定

# 要員人数
staff_number_entry = create_label_entry(contract_info_frame, "要員人数", 0, 0)

# 契約単価（円）のフレーム
contract_price_frame = tk.LabelFrame(contract_info_frame, text="▶契約単価（円）")

# 月間標準
standard_monthly_entry = create_label_entry(contract_price_frame, "月間標準", 0, 0)

# 追加
additional_entry = create_label_entry(contract_price_frame, "追加", 1, 0)

# 取消
cancellation_entry = create_label_entry(contract_price_frame, "取消", 2, 0)

# 作業時間（時）のフレーム
working_hours_frame = tk.LabelFrame(contract_info_frame, text="▶作業時間（時）")

# 基本作業時間
basic_working_hours_entry = create_label_entry(working_hours_frame, "基本", 0, 0)

# 追加発生作業時間
additional_working_hours_entry = create_label_entry(working_hours_frame, "追加発生", 1, 0)

# 取消発生作業時間
cancellation_working_hours_entry = create_label_entry(working_hours_frame, "取消発生", 2, 0)

# 原価情報のフレーム
cost_info_frame = tk.LabelFrame(contract_info_frame, text="▶原価情報")

# 格
grade_dropdown = create_label_dropdown(cost_info_frame, "格", ["A", "B", "C"], 0, 0)

# 基本原価
basic_cost_entry = create_label_entry(cost_info_frame, "基本", 1, 0)

# 追加発生原価
additional_cost_entry = create_label_entry(cost_info_frame, "追加発生", 2, 0)

# 取消発生原価
cancellation_cost_entry = create_label_entry(cost_info_frame, "取消発生", 3, 0)

# 工数のフレーム
# ...


# 要員名
# 要員人数のエントリーが変更されたときに実行されるコールバック関数を設定する
staff_number_entry.bind("<KeyRelease>", lambda event: update_staff_entries())

# アプリケーション起動時にフレームの位置を初期化する
update_staff_entries()

############################################################################################

# アプリケーションを実行
root.mainloop()

