---
title: 'Mongo Replica Set based Chat'
disqus: hackmd
---

Mongo Replica Set based Chat
===
![downloads](https://img.shields.io/github/downloads/atom/atom/total.svg)

## Table of Contents

[TOC]

## Before shutdown of primary mongodb instance


### rs.config()
---
```
rs0:PRIMARY> rs.config()
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "mongo1:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "mongo2:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "mongo3:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {

		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5db871de4ec3072b7ae303dc")
	}
}
```

### rs.status()
---
```
rs0:PRIMARY> rs.status()
{
	"set" : "rs0",
	"date" : ISODate("2019-10-29T22:41:43.729Z"),
	"myState" : 1,
	"term" : NumberLong(3),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572388899, 1),
			"t" : NumberLong(3)
		},
		"lastCommittedWallTime" : ISODate("2019-10-29T22:41:39.174Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572388899, 1),
			"t" : NumberLong(3)
		},
		"readConcernMajorityWallTime" : ISODate("2019-10-29T22:41:39.174Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572388899, 1),
			"t" : NumberLong(3)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572388899, 1),
			"t" : NumberLong(3)
		},
		"lastAppliedWallTime" : ISODate("2019-10-29T22:41:39.174Z"),
		"lastDurableWallTime" : ISODate("2019-10-29T22:41:39.174Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572388869, 5),
	"lastStableCheckpointTimestamp" : Timestamp(1572388869, 5),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "electionTimeout",
		"lastElectionDate" : ISODate("2019-10-29T21:41:20.324Z"),
		"termAtElection" : NumberLong(3),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(0, 0),
			"t" : NumberLong(-1)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572374573, 1),
			"t" : NumberLong(1)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"numCatchUpOps" : NumberLong(27017),
		"newTermStartDate" : ISODate("2019-10-29T21:41:20.578Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-10-29T21:41:21.798Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "mongo1:27017",
			"ip" : "172.31.16.94",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 3634,
			"optime" : {
				"ts" : Timestamp(1572388899, 1),
				"t" : NumberLong(3)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572388899, 1),
				"t" : NumberLong(3)
			},
			"optimeDate" : ISODate("2019-10-29T22:41:39Z"),
			"optimeDurableDate" : ISODate("2019-10-29T22:41:39Z"),
			"lastHeartbeat" : ISODate("2019-10-29T22:41:43.027Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-29T22:41:42.597Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "mongo2:27017",
			"syncSourceHost" : "mongo2:27017",
			"syncSourceId" : 1,
			"infoMessage" : "",
			"configVersion" : 1
		},
		{
			"_id" : 1,
			"name" : "mongo2:27017",
			"ip" : "172.31.26.99",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 3635,
			"optime" : {
				"ts" : Timestamp(1572388899, 1),
				"t" : NumberLong(3)
			},
			"optimeDate" : ISODate("2019-10-29T22:41:39Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572385280, 1),
			"electionDate" : ISODate("2019-10-29T21:41:20Z"),
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 2,
			"name" : "mongo3:27017",
			"ip" : "172.31.46.232",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 3603,
			"optime" : {
				"ts" : Timestamp(1572388899, 1),
				"t" : NumberLong(3)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572388899, 1),
				"t" : NumberLong(3)
			},
			"optimeDate" : ISODate("2019-10-29T22:41:39Z"),
			"optimeDurableDate" : ISODate("2019-10-29T22:41:39Z"),
			"lastHeartbeat" : ISODate("2019-10-29T22:41:42.122Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-29T22:41:41.958Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "mongo2:27017",
			"syncSourceHost" : "mongo2:27017",
			"syncSourceId" : 1,
			"infoMessage" : "",
			"configVersion" : 1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572388899, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572388899, 1)
}
```
### Screenshot of the app

![](https://i.imgur.com/7Zym7pX.png)


## After shutdown of primary mongodb instance

### rs.config()
```
rs0:PRIMARY> rs.config()
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "mongo1:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "mongo2:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "mongo3:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {

		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5db871de4ec3072b7ae303dc")
	}
}
```
### rs.status()
```
rs0:PRIMARY> rs.status()
{
	"set" : "rs0",
	"date" : ISODate("2019-10-29T22:50:56.519Z"),
	"myState" : 1,
	"term" : NumberLong(4),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572389453, 1),
			"t" : NumberLong(4)
		},
		"lastCommittedWallTime" : ISODate("2019-10-29T22:50:53.694Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572389453, 1),
			"t" : NumberLong(4)
		},
		"readConcernMajorityWallTime" : ISODate("2019-10-29T22:50:53.694Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572389453, 1),
			"t" : NumberLong(4)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572389453, 1),
			"t" : NumberLong(4)
		},
		"lastAppliedWallTime" : ISODate("2019-10-29T22:50:53.694Z"),
		"lastDurableWallTime" : ISODate("2019-10-29T22:50:53.694Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572389437, 2),
	"lastStableCheckpointTimestamp" : Timestamp(1572389437, 2),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "stepUpRequestSkipDryRun",
		"lastElectionDate" : ISODate("2019-10-29T22:47:33.136Z"),
		"termAtElection" : NumberLong(4),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(1572389250, 1),
			"t" : NumberLong(3)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572389250, 1),
			"t" : NumberLong(3)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"priorPrimaryMemberId" : 1,
		"numCatchUpOps" : NumberLong(27017),
		"newTermStartDate" : ISODate("2019-10-29T22:47:33.688Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-10-29T22:47:34.223Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "mongo1:27017",
			"ip" : "172.31.16.94",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 4220,
			"optime" : {
				"ts" : Timestamp(1572389453, 1),
				"t" : NumberLong(4)
			},
			"optimeDate" : ISODate("2019-10-29T22:50:53Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572389253, 1),
			"electionDate" : ISODate("2019-10-29T22:47:33Z"),
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 1,
			"name" : "mongo2:27017",
			"ip" : "172.31.26.99",
			"health" : 0,
			"state" : 8,
			"stateStr" : "(not reachable/healthy)",
			"uptime" : 0,
			"optime" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDate" : ISODate("1970-01-01T00:00:00Z"),
			"optimeDurableDate" : ISODate("1970-01-01T00:00:00Z"),
			"lastHeartbeat" : ISODate("2019-10-29T22:50:51.075Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-29T22:47:33.092Z"),
			"pingMs" : NumberLong(1),
			"lastHeartbeatMessage" : "Error connecting to mongo2:27017 (172.31.26.99:27017) :: caused by :: No route to host",
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"configVersion" : -1
		},
		{
			"_id" : 2,
			"name" : "mongo3:27017",
			"ip" : "172.31.46.232",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 4156,
			"optime" : {
				"ts" : Timestamp(1572389453, 1),
				"t" : NumberLong(4)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572389453, 1),
				"t" : NumberLong(4)
			},
			"optimeDate" : ISODate("2019-10-29T22:50:53Z"),
			"optimeDurableDate" : ISODate("2019-10-29T22:50:53Z"),
			"lastHeartbeat" : ISODate("2019-10-29T22:50:55.240Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-29T22:50:56.324Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "mongo1:27017",
			"syncSourceHost" : "mongo1:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572389453, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572389453, 1)
}
```
### Screenshot of the app

![](https://i.imgur.com/iOWzAfK.png)

