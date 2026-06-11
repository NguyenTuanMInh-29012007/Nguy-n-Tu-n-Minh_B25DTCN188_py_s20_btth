import unittest
from main import calculate_total_revenue

class TestTicketingSystem(unittest.TestCase):
    """Lớp kiểm thử cho các hàm xử lý tính toán của Hệ Thống Quản Lý Vé Rikkei Esports."""

    def test_calculate_revenue_mixed_status(self):
        """Test Case 1: Danh sách có cả vé Booked và Cancelled.
        Hàm phải trả về đúng tổng tiền của các vé có trạng thái 'Booked'.
        """
        mock_tickets = [
            {"ticket_id": "T01", "buyer_name": "Nguyen Van A", "price": 500.0, "status": "Booked", "seat": ("A", 1)},
            {"ticket_id": "T02", "buyer_name": "Tran Thi B", "price": 300.0, "status": "Cancelled", "seat": ("B", 5)},
            {"ticket_id": "T03", "buyer_name": "Le Van C", "price": 500.0, "status": "Booked", "seat": ("A", 2)},
            {"ticket_id": "T04", "buyer_name": "Pham Van D", "price": 400.0, "status": "Cancelled", "seat": ("C", 10)}
        ]

        expected_revenue = 1000.0
        actual_revenue = calculate_total_revenue(mock_tickets)
        
        self.assertEqual(actual_revenue, expected_revenue, "Lỗi: Hàm tính sai doanh thu khi có vé bị hủy!")

    def test_calculate_revenue_empty_list(self):
        """Test Case 2: Danh sách vé trống [].
        Hàm phải trả về giá trị là 0.0.
        """
        mock_tickets = []
        expected_revenue = 0.0
        actual_revenue = calculate_total_revenue(mock_tickets)
        
        self.assertEqual(actual_revenue, expected_revenue, "Lỗi: Hàm phải trả về 0.0 khi danh sách vé rỗng!")

    def test_calculate_revenue_all_cancelled(self):
        """Test Case bổ sung: Tất cả các vé trong danh sách đều bị hủy (Cancelled).
        Hàm phải trả về giá trị là 0.0.
        """
        mock_tickets = [
            {"ticket_id": "T01", "buyer_name": "Nguyen Van A", "price": 500.0, "status": "Cancelled", "seat": ("A", 1)},
            {"ticket_id": "T02", "buyer_name": "Tran Thi B", "price": 300.0, "status": "Cancelled", "seat": ("B", 5)}
        ]
        expected_revenue = 0.0
        actual_revenue = calculate_total_revenue(mock_tickets)
        
        self.assertEqual(actual_revenue, expected_revenue, "Lỗi: Hàm phải trả về 0.0 khi tất cả vé đều bị hủy!")

if __name__ == "__main__":
    unittest.main()