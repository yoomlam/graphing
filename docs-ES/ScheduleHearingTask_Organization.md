| [README.md](/README.md) | [Task Listing](tasklist.md) |

# ScheduleHearingTask_Organization

## Tasks Created Before and After

<details><summary>Tasks created before and after ScheduleHearingTask_Organization</summary>

```
digraph G {
rankdir="LR";
"DistributionTask_Organization" -> "ScheduleHearingTask_Organization" [label=128]
"ScheduleHearingTask_Organization" -> "HearingTask_Organization" [label=128]
}
```
</details>

![ScheduleHearingTask_Organization](dot/ScheduleHearingTask_Organization.dot.png)

**Before:**

   * [DistributionTask_Organization](DistributionTask_Organization.md): 128 times

**After:**

   * [HearingTask_Organization](HearingTask_Organization.md): 128 times

## Task Creation Sequences

### RTO.TVTO.DTO.SHTO

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

![RTO.TVTO.DTO.SHTO-42769](uml/RTO.TVTO.DTO.SHTO-42769.png)

### RTO.DTO.SHTO

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

![RTO.DTO.SHTO-41136](uml/RTO.DTO.SHTO-41136.png)

