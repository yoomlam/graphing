| [README.md](/README.md) | [Task Listing](tasklist.md) |

# SpecialCaseMovementTask_User

## Tasks Created Before and After

<details><summary>Tasks created before and after SpecialCaseMovementTask_User</summary>

```
digraph G {
rankdir="LR";
"SpecialCaseMovementTask_User" -> "JudgeAssignTask_User" [label=1]
"DistributionTask_Organization" -> "SpecialCaseMovementTask_User" [label=1]
}
```
</details>

![SpecialCaseMovementTask_User](dot/SpecialCaseMovementTask_User.dot.png)

**Before:**

   * [DistributionTask_Organization](DistributionTask_Organization.md): 1 times

**After:**

   * [JudgeAssignTask_User](JudgeAssignTask_User.md): 1 times

## Task Creation Sequences

### RTO.DTO.SCMTU

1 occurrences (example appeal IDs: [41963])

<details><summary>Task Tree for appeal with ID 41963</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.DistributionTask_Organization #fc8d62
object 2.SpecialCaseMovementTask_User #a6d854
object 3.JudgeAssignTask_User #8da0cb
0.RootTask_Organization -- 1.DistributionTask_Organization
1.DistributionTask_Organization -- 2.SpecialCaseMovementTask_User
0.RootTask_Organization -- 3.JudgeAssignTask_User
@enduml
```
</details>

![RTO.DTO.SCMTU-41963](uml/RTO.DTO.SCMTU-41963.png)

