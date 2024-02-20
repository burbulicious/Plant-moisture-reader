from simlulator import simulate_metrics
from unittest.mock import patch

def test_simulate_metrics():
    with patch('random.randint', side_effect=[20, 500]):
        metrics = simulate_metrics()
        assert metrics == {"moisture": 20, "temperature": 500}