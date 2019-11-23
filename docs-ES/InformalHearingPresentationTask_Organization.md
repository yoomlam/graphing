| [README.md](/README.md) | [Task Listing](tasklist.md) |

# InformalHearingPresentationTask_Organization

## Tasks Created Before and After

<details><summary>Tasks created before and after InformalHearingPresentationTask_Organization</summary>

```
digraph G {
rankdir="LR";
"InformalHearingPresentationTask_Organization" -> "InformalHearingPresentationTask_User" [label=3]
"InformalHearingPresentationTask_Organization" -> "JudgeAssignTask_User" [label=1]
"EvidenceSubmissionWindowTask_Organization" -> "InformalHearingPresentationTask_Organization" [label=9]
}
```
</details>

![InformalHearingPresentationTask_Organization](dot/InformalHearingPresentationTask_Organization.dot.png)

**Before:**

   * [EvidenceSubmissionWindowTask_Organization](EvidenceSubmissionWindowTask_Organization.md): 9 times

**After:**

   * [InformalHearingPresentationTask_User](InformalHearingPresentationTask_User.md): 3 times
   * [JudgeAssignTask_User](JudgeAssignTask_User.md): 1 times

## Task Creation Sequences

### RTO.TVTO.DTO.ESWTO.IHPTO

9 occurrences (example appeal IDs: [40596, 15370, 42548, 41133, 40540])

<details><summary>Task Tree for appeal with ID 40596</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.TrackVeteranTask_Organization #8da0cb
object 2.DistributionTask_Organization #fc8d62
object 3.EvidenceSubmissionWindowTask_Organization #b3b3b3
object 4.InformalHearingPresentationTask_Organization #ffd92f
0.RootTask_Organization -- 1.TrackVeteranTask_Organization
0.RootTask_Organization -- 2.DistributionTask_Organization
2.DistributionTask_Organization -- 3.EvidenceSubmissionWindowTask_Organization
2.DistributionTask_Organization -- 4.InformalHearingPresentationTask_Organization
@enduml
```
</details>

![RTO.TVTO.DTO.ESWTO.IHPTO-40596](uml/RTO.TVTO.DTO.ESWTO.IHPTO-40596.png)

