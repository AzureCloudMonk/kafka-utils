from mock import sentinel
import pytest

from yelp_kafka_tool.kafka_cluster_manager.cluster_info.partition import Partition


class TestPartition(object):

    @pytest.fixture
    def partition(self):
        return Partition(
            ('p1', 0),
            sentinel.topic1,
            [sentinel.r1, sentinel.r2],
        )

    def test_name(self, partition):
        assert partition.name == ('p1', 0)

    def test_topic(self, partition):
        assert partition.topic == sentinel.topic1

    def test_replicas(self, partition):
        assert partition.replicas == [sentinel.r1, sentinel.r2]

    def test_leader(self, partition):
        assert partition.leader == sentinel.r1

    def test_replication_factor(self, partition):
        assert partition.replication_factor() == 2

    def test_partition_id(self, partition):
        assert partition.partition_id == 0
