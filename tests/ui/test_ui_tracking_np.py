from modules.ui.page_objects.tracking_nova_poshta import TrackingNovaPoshta
import pytest

@pytest.mark.my_ui2
def test_correct_number():
    tracking_nova_poshta = TrackingNovaPoshta()

    tracking_nova_poshta.go_to()

    tracking_nova_poshta.try_to_track_parcel("20450669380383")

    assert tracking_nova_poshta.check_title("Трекінг Нова пошта - відстежити посилку, відслідковувати ТТН")
    
    tracking_nova_poshta.close()
