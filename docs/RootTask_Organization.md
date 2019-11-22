| [README.md](README.md) | [Task Listing](tasklist.md) |

# RootTask_Organization

## Tasks Created Before and After

<details><summary>Tasks created before and after RootTask_Organization</summary>

```
digraph G {
rankdir="LR";
"RootTask_Organization" -> "DistributionTask_Organization" [label=102]
"RootTask_Organization" -> "TrackVeteranTask_Organization" [label=301]
}
```
</details>

![RootTask_Organization](dot/RootTask_Organization.dot.png)

**Before:**


**After:**

   * [TrackVeteranTask_Organization](TrackVeteranTask_Organization.md): 301 times
   * [DistributionTask_Organization](DistributionTask_Organization.md): 102 times

## Task Creation Sequences

### RTO

403 occurrences (example appeal IDs: [42769, 34538, 39812, 41319, 15152])

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

![RTO-42769](uml/RTO-42769.png)

