| [README.md](README.md) | [Task Listing](tasklist.md) |

# HearingTask_Organization

## Tasks Created Before and After

<details><summary>Tasks created before and after HearingTask_Organization</summary>

```
digraph G {
rankdir="LR";
"HearingTask_Organization" -> "HearingAdminActionVerifyAddressTask_Organization" [label=3]
"ScheduleHearingTask_Organization" -> "HearingTask_Organization" [label=128]
"HearingTask_Organization" -> "AssignHearingDispositionTask_Organization" [label=3]
"HearingTask_Organization" -> "TrackVeteranTask_Organization" [label=1]
"HearingTask_Organization" -> "TranslationTask_Organization" [label=1]
"HearingTask_Organization" -> "ReturnedUndeliverableCorrespondenceMailTask_Organization" [label=1]
}
```
</details>

![HearingTask_Organization](dot/HearingTask_Organization.dot.png)

**Before:**

   * [ScheduleHearingTask_Organization](ScheduleHearingTask_Organization.md): 128 times

**After:**

   * [AssignHearingDispositionTask_Organization](AssignHearingDispositionTask_Organization.md): 3 times
   * [HearingAdminActionVerifyAddressTask_Organization](HearingAdminActionVerifyAddressTask_Organization.md): 3 times
   * [TrackVeteranTask_Organization](TrackVeteranTask_Organization.md): 1 times
   * [TranslationTask_Organization](TranslationTask_Organization.md): 1 times
   * [ReturnedUndeliverableCorrespondenceMailTask_Organization](ReturnedUndeliverableCorrespondenceMailTask_Organization.md): 1 times

## Task Creation Sequences

### RTO.TVTO.DTO.SHTO.HTO

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

![RTO.TVTO.DTO.SHTO.HTO-42769](uml/RTO.TVTO.DTO.SHTO.HTO-42769.png)

### RTO.DTO.SHTO.HTO

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

![RTO.DTO.SHTO.HTO-41136](uml/RTO.DTO.SHTO.HTO-41136.png)

