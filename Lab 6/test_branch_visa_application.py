import pytest
from visa_application import visa_fee, documents_complete, application_status

def test_within_included_entries():
    assert visa_fee("tourist", 1, "normal", "B") == 0

def test_excluded_entries():
    with pytest.raises(ValueError,match="unknown visa type"):
        visa_fee("tour",1,"normal","B")

def test_invalid_entries():
    with pytest.raises(ValueError,match="invalid entries"):
        visa_fee("tourist",-1,"normal","B")


def test_A_not_student():
    assert visa_fee("tourist", 1, "normal", "A") == 0

def test_A_student():
    assert visa_fee("student", 3, "normal", "A") == 40

def test_extra():
    assert visa_fee("tourist",3,"normal","A")==40

def test_express():
    assert visa_fee("tourist",3,"express","B")==200

def test_over_5_extra():
    assert visa_fee("tourist",8,"normal","A")==360


def test_over_5_extra_express():
    assert visa_fee("tourist",8,"express","A")==780

def test_doc_complete_renewed():
    assert documents_complete(3,2,True) is True

def test_doc_complete_renewed_unfilled():
    assert documents_complete(0,2,True) is False

def test_doc_complete_unrenewed_with_photos_with_forms():
    assert documents_complete(3,2,False) is True

def test_doc_complete_unrenewed_without_photos():
    assert documents_complete(3,0,False) is False

def test_doc_complete_unrenewed_with_photos_without_forms():
        assert documents_complete(2,2,False) is False

def test_application():
    assert application_status(30,True,False) == "open"

def test_application_unexpress():
    assert application_status(50,False,False) == "open"
    assert application_status(15, False, False) == "closing"
    assert application_status(10, False, False) == "closed"


def test_application_express():
    assert application_status(50,True,False) == "open"
    assert application_status(5, True, False) == "closing"
    assert application_status(0, True, False) == "closing"

def test_application_unexpress_with_peak():
    assert application_status(50,False,True) == "open"
    assert application_status(30, False, True) == "closing"
    assert application_status(20, False, True) == "closed"


def test_application_express_with_peak():
    assert application_status(50, True, True) == "open"
    assert application_status(10, True, True) == "closing"
    assert application_status(5, True, True) == "closed"
