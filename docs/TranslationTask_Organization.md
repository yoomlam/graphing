| [README.md](README.md) | [Task Listing](tasklist.md) |

# TranslationTask_Organization

## Tasks Created Before and After

<details><summary>Tasks created before and after TranslationTask_Organization</summary>

```
digraph G {
rankdir="LR";
"HearingTask_Organization" -> "TranslationTask_Organization" [label=1]
"TranslationTask_Organization" -> "TranslationTask_User" [label=1]
"DistributionTask_Organization" -> "TranslationTask_Organization" [label=1]
}
```
</details>

![TranslationTask_Organization](dot/TranslationTask_Organization.dot.png)

**Before:**

   * [DistributionTask_Organization](DistributionTask_Organization.md): 1 times
   * [HearingTask_Organization](HearingTask_Organization.md): 1 times

**After:**

   * [TranslationTask_User](TranslationTask_User.md): 1 times

## Task Creation Sequences

### RTO.DTO.TTO

1 occurrences (example appeal IDs: [41094])

<details><summary>Task Tree for appeal with ID 41094</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.DistributionTask_Organization #fc8d62
object 2.TranslationTask_Organization #e5c494
0.RootTask_Organization -- 1.DistributionTask_Organization
1.DistributionTask_Organization -- 2.TranslationTask_Organization
@enduml
```
</details>

![RTO.DTO.TTO-41094](uml/RTO.DTO.TTO-41094.png)

### RTO.DTO.SHTO.HTO.TTO

1 occurrences (example appeal IDs: [24900])

<details><summary>Task Tree for appeal with ID 24900</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.DistributionTask_Organization #fc8d62
object 2.ScheduleHearingTask_Organization #a6d854
object 3.HearingTask_Organization #e78ac3
object 4.TranslationTask_Organization #e5c494
object 5.HearingAdminActionVerifyAddressTask_Organization #e78ac3
object 6.TranslationTask_User #e5c494
0.RootTask_Organization -- 1.DistributionTask_Organization
3.HearingTask_Organization -- 2.ScheduleHearingTask_Organization
1.DistributionTask_Organization -- 3.HearingTask_Organization
1.DistributionTask_Organization -- 4.TranslationTask_Organization
2.ScheduleHearingTask_Organization -- 5.HearingAdminActionVerifyAddressTask_Organization
4.TranslationTask_Organization -- 6.TranslationTask_User
@enduml
```
</details>

![RTO.DTO.SHTO.HTO.TTO-24900](uml/RTO.DTO.SHTO.HTO.TTO-24900.png)

