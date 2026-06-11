import logging

logging.basicConfig(
    filename="arena_tickets.log",
    format="[%(asctime)s] - [%(levelname)s] - %(message)s",
    level=logging.INFO,
)

tickets = [
    {
        "ticket_id": "T01",
        "buyer_name": "Nguyen Van A",
        "price": 500.0,
        "status": "Booked",
        "seat": ("A", 1),
    },
    {
        "ticket_id": "T02",
        "buyer_name": "Tran Thi B",
        "price": 300.0,
        "status": "Cancelled",
        "seat": ("B", 5),
    },
    {
        "ticket_id": "T03",
        "buyer_name": "Le Van C",
        "price": 500.0,
        "status": "Booked",
        "seat": ("A", 2),
    },
]


def display_tickets(tickets):
    if not tickets:
        print("Danh sách đang trống!")
    else:
        print("------ DANH SÁCH VÉ ------")
        print(
            f"{'Mã Vé':<5} | {'Tên Khách Hàng':<15} | {'Giá Vé':<5} | {'Chỗ Ngồi':<5} | {'Trạng thái':<10}"
        )
        print("-" * 60)

        for ticket in tickets:
            try:
                seat = f"{ticket['seat'][0]}-{ticket['seat'][1]}"
                print(
                    f"{ticket['ticket_id']:<5} | {ticket['buyer_name']:<15} | {ticket['price']:<6} | {seat:<8} | {ticket['status']:<10}"
                )
            except KeyError as key:
                print("Lỗi: Một vé đang bị thiếu dữ liệu, vui lòng kiểm tra lại.")
                logging.error(f"Missing key while displaying ticket {key}")

        logging.info("User viewed ticket list.")
        print("-" * 60)


def book_ticket(tickets):
    print("--- ĐẶT VÉ MỚI ---")

    ticket_id = input("Nhập mã trận đấu: ").strip().upper()

    if not ticket_id:
        print("Mã vé không được để trống.")
        logging.warning("User tried to add a ticket with empty ticket ID.")
        return

    for ticket in tickets:
        if ticket_id == ticket["ticket_id"]:
            print(f"Lỗi: Mã trận đấu {ticket_id} đã tồn tại.")
            logging.warning(f"Duplicate ticket ID entered: {ticket_id}")
            return

    buyer_name = input("Nhập tên khách hàng: ").strip().title()
    while buyer_name == "":
        buyer_name = (
            input("Tên khách hàng không được để trống! Vui lòng nhập lại: ")
            .strip()
            .title()
        )

    while True:
        try:
            price = int(input("Nhập giá vé: "))
            if price <= 0:
                price = int(
                    input("Giá tiền nhập không hợp lệ! Vui lòng nhập lại (>0): ")
                )
                continue
            else:
                break
        except ValueError:
            print("Giá tiền phải nhập dạng số nguyên!")
            logging.warning("Invalid price input while booking ticket")

    seat_id = input("Nhập khu vực ghế: ").strip().upper()
    while seat_id == "":
        seat_id = (
            input("[Lỗi] Khu vực ghế không được để trống! Vui lòng nhập lại: ")
            .strip()
            .upper()
        )

    while True:
        try:
            quantity = int(input("Nhập số ghế: "))
            if quantity <= 0:
                quantity = int(
                    input("Số lượng nhập không hợp lệ! Vui lòng nhập lại (>0): ")
                )
                continue
            else:
                break
        except ValueError:
            print("Số lượng phải nhập dạng số nguyên!")
            logging.warning("Invalid quantity input while booking ticket")

    seat = (seat_id, quantity)

    new_ticket = {
        "ticket_id": ticket_id,
        "buyer_name": buyer_name,
        "price": price,
        "status": "Booked",
        "seat": seat,
    }

    tickets.append(new_ticket)

    print(f"Thành công: Đã đặt vé {ticket_id}.")
    logging.info(f"Booked new ticket {ticket_id} for {buyer_name}")


def change_seat(tickets):
    print("--- ĐỔI CHỖ NGỒI ---")

    ticket_id = input("Nhập mã vé cần đổi chỗ: ").strip().upper()

    if not ticket_id:
        print("Mã vé không được để trống.")
        logging.warning("User tried to add a ticket with empty ticket ID.")
        return
    found = False
    for ticket in tickets:
        if ticket_id == ticket["ticket_id"]:
            found = True
            seat_id = input("Nhập khu vực ghế mới: ").strip().upper()
            while seat_id == "":
                seat_id = (
                    input("[Lỗi] Khu vực ghế không được để trống! Vui lòng nhập lại: ")
                    .strip()
                    .upper()
                )

            while True:
                try:
                    quantity = int(input("Nhập số ghế mới: "))
                    if quantity <= 0:
                        quantity = int(
                            input(
                                "Số lượng nhập không hợp lệ! Vui lòng nhập lại (>0): "
                            )
                        )
                        continue
                    else:
                        break
                except ValueError:
                    print("Số lượng phải nhập dạng số nguyên!")
                    logging.warning("Invalid quantity input while booking ticket")

            ticket["seat"] = (seat_id, quantity)

            print(
                f"Thành công: Đã đổi chỗ vé {ticket_id} sang ({ticket['seat'][0]}-{ticket['seat'][1]})."
            )
            logging.info(
                f"Seat changed for ticket {ticket_id} to {ticket['seat'][0]}-{ticket['seat'][1]}"
            )
    if not found:
        print(f"Không tìm thấy MÃ {ticket_id}!")
        logging.warning(f"Change seat failed - Ticket {ticket_id} not found")


def cancel_ticket(tickets):
    print("--- HỦY VÉ ---")

    ticket_id = input("Nhập mã vé cần hủy: ").strip().upper()

    if not ticket_id:
        print("Mã vé không được để trống.")
        logging.warning("User tried to add a ticket with empty ticket ID.")
        return
    found = False
    for ticket in tickets:
        if ticket_id == ticket["ticket_id"]:
            found = True
            if ticket["status"] != "Cancelled":
                ticket["status"] = "Cancelled"
                print(f"Đã hủy thành công Mã {ticket_id}")
                logging.warning(f"Ticket {ticket_id} has been cancelled.")
            else:
                print(f"Vé {ticket_id} đã ở trạng thái Cancelled trước đó.")
        break

    if not found:
        print(f"Không tìm thấy MÃ {ticket_id}!")
        logging.warning(f"Cancel ticket failed - Ticket {ticket_id} not found")


def calculate_revenue(tickets):
    count_booked = 0
    count_cancelled = 0
    total_price = 0
    
    for ticket in tickets:
        try:
            if ticket["status"] == "Booked":
                count_booked += 1
                total_price += ticket['price']
            else:
                count_cancelled += 1
            
        except KeyError as key:
            print("[Lỗi]: Một vé đang bị thiếu dữ liệu doanh thu")
            logging.error(f"Missing key while calculating revenue: '{key}'")

    print("--- BÁO CÁO DOANH THU ---")
    print(f"Tổng số vé đã đặt: {count_booked}")
    print(f"Tổng số vé đã hủy: {count_cancelled}")
    print(f"Tổng doanh thu hợp lệ: {total_price:.1f}")
    logging.info(f"Revenue report generated. Total: {total_price:.1f}")
    

def main():
    while True:
        choice = input("""
    === HỆ THỐNG QUẢN LÝ VÉ RIKKEI ESPORTS ===
    1. Xem danh sách vé đã bán
    2. Đặt vé mới
    3. Đổi chỗ ngồi (Cập nhật vé)
    4. Hủy vé
    5. Báo cáo doanh thu
    6. Thoát chương trình
    ======================================== 
    Chọn chức năng (1-6): """)

        match choice:
            case "1":
                display_tickets(tickets)
            case "2":
                book_ticket(tickets)
            case "3":
                change_seat(tickets)
            case "4":
                cancel_ticket(tickets)
            case "5":
                calculate_revenue(tickets)
            case "6":
                logging.info("Ticket management system closed.")
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý vé Rikkei Esports. ")
                break
            case _:
                print("Lựa chọn không hợp lệ! Vui lòng nhập lại (1-6): ")
                logging.warning("Invalid menu choice selected")


if __name__ == "__main__":
    main()
