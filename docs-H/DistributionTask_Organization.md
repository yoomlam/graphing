| [README.md](/README.md) | [Task Listing](tasklist.md) |

# DistributionTask_Organization

## Tasks Created Before and After

<details><summary>Tasks created before and after DistributionTask_Organization</summary>

```
digraph G {
rankdir="LR";
"DistributionTask_Organization" -> "ScheduleHearingTask_Organization" [label=128]
"RootTask_Organization" -> "DistributionTask_Organization" [label=9]
"TrackVeteranTask_Organization" -> "DistributionTask_Organization" [label=119]
}
```
</details>

![DistributionTask_Organization](dot/DistributionTask_Organization.dot.png)

**Before:**

   * [TrackVeteranTask_Organization](TrackVeteranTask_Organization.md): 119 times
   * [RootTask_Organization](RootTask_Organization.md): 9 times

**After:**

   * [ScheduleHearingTask_Organization](ScheduleHearingTask_Organization.md): 128 times

## Task Creation Sequences

### RTO.TVTO.DTO

119 occurrences (example appeal IDs: [42769, 42820, 42010, 42071, 39818])

<details><summary>Task Tree for appeal with ID 42769</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.TrackVeteranTask_Organization #8da0cb
object 2.DistributionTask_Organization #fc8d62
object 3.ScheduleHearingTask_Organization #a6d854
object 4.HearingTask_Organization #e78ac3
0.RootTask_Organization -- 1.TrackVeteranTask_Organization
0.RootTask_Organization -- 2.DistributionTask_Organization
4.HearingTask_Organization -- 3.ScheduleHearingTask_Organization
2.DistributionTask_Organization -- 4.HearingTask_Organization
@enduml
```
</details>

![RTO.TVTO.DTO-42769](uml/RTO.TVTO.DTO-42769.png)

### RTO.DTO

9 occurrences (example appeal IDs: [41136, 42097, 4988, 42691, 40835])

<details><summary>Task Tree for appeal with ID 41136</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.DistributionTask_Organization #fc8d62
object 2.ScheduleHearingTask_Organization #a6d854
object 3.HearingTask_Organization #e78ac3
0.RootTask_Organization -- 1.DistributionTask_Organization
3.HearingTask_Organization -- 2.ScheduleHearingTask_Organization
1.DistributionTask_Organization -- 3.HearingTask_Organization
@enduml
```
</details>

![RTO.DTO-41136](uml/RTO.DTO-41136.png)

