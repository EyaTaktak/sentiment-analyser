from app.models import CustomerFeedback


def test_customer_feedback_schema():
    data = {
        "product_category": "Electronics",
        "sentiment": "Negative",
        "store_location": "Paris",
        "is_complaint": True,
    }

    feedback = CustomerFeedback(**data)

    assert feedback.is_complaint is True
    assert feedback.sentiment == "Negative"
