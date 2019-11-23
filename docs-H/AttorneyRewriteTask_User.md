| [README.md](/README.md) | [Task Listing](tasklist.md) |

# AttorneyRewriteTask_User

## Tasks Created Before and After

<details><summary>Tasks created before and after AttorneyRewriteTask_User</summary>

```
digraph G {
rankdir="LR";
"AttorneyTask_User" -> "AttorneyRewriteTask_User" [label=4]
"AttorneyRewriteTask_User" -> "BvaDispatchTask_Organization" [label=4]
}
```
</details>

![AttorneyRewriteTask_User](dot/AttorneyRewriteTask_User.dot.png)

**Before:**

   * [AttorneyTask_User](AttorneyTask_User.md): 4 times

**After:**

   * [BvaDispatchTask_Organization](BvaDispatchTask_Organization.md): 4 times

## Task Creation Sequences

### RTO.TVTO.DTO.ESWTO.IHPTO.JATU.JDRTU.ATU.ARTU

2 occurrences (example appeal IDs: [11522, 11522])

<details><summary>Task Tree for appeal with ID 11522</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.TrackVeteranTask_Organization #8da0cb
object 2.DistributionTask_Organization #fc8d62
object 3.EvidenceSubmissionWindowTask_Organization #b3b3b3
object 4.InformalHearingPresentationTask_Organization #ffd92f
object 5.JudgeAssignTask_User #8da0cb
object 6.JudgeDecisionReviewTask_User #66c2a5
object 7.AttorneyTask_User #fc8d62
object 8.AttorneyRewriteTask_User #8da0cb
object 9.BvaDispatchTask_Organization #e5c494
object 10.BvaDispatchTask_User #e5c494
0.RootTask_Organization -- 1.TrackVeteranTask_Organization
0.RootTask_Organization -- 2.DistributionTask_Organization
2.DistributionTask_Organization -- 3.EvidenceSubmissionWindowTask_Organization
2.DistributionTask_Organization -- 4.InformalHearingPresentationTask_Organization
0.RootTask_Organization -- 5.JudgeAssignTask_User
0.RootTask_Organization -- 6.JudgeDecisionReviewTask_User
6.JudgeDecisionReviewTask_User -- 7.AttorneyTask_User
6.JudgeDecisionReviewTask_User -- 8.AttorneyRewriteTask_User
0.RootTask_Organization -- 9.BvaDispatchTask_Organization
9.BvaDispatchTask_Organization -- 10.BvaDispatchTask_User
@enduml
```
</details>

![RTO.TVTO.DTO.ESWTO.IHPTO.JATU.JDRTU.ATU.ARTU-11522](uml/RTO.TVTO.DTO.ESWTO.IHPTO.JATU.JDRTU.ATU.ARTU-11522.png)

### RTO.DTO.ESWTO.SCMTU.JATU.JDRTU.ATU.ARTU

2 occurrences (example appeal IDs: [40605, 40605])

<details><summary>Task Tree for appeal with ID 40605</summary>

```
@startuml
object 0.RootTask_Organization #66c2a5
object 1.DistributionTask_Organization #fc8d62
object 2.EvidenceSubmissionWindowTask_Organization #b3b3b3
object 3.SpecialCaseMovementTask_User #a6d854
object 4.JudgeAssignTask_User #8da0cb
object 5.JudgeDecisionReviewTask_User #66c2a5
object 6.AttorneyTask_User #fc8d62
object 7.AttorneyRewriteTask_User #8da0cb
object 8.BvaDispatchTask_Organization #e5c494
object 9.BvaDispatchTask_User #e5c494
0.RootTask_Organization -- 1.DistributionTask_Organization
1.DistributionTask_Organization -- 2.EvidenceSubmissionWindowTask_Organization
1.DistributionTask_Organization -- 3.SpecialCaseMovementTask_User
0.RootTask_Organization -- 4.JudgeAssignTask_User
0.RootTask_Organization -- 5.JudgeDecisionReviewTask_User
5.JudgeDecisionReviewTask_User -- 6.AttorneyTask_User
5.JudgeDecisionReviewTask_User -- 7.AttorneyRewriteTask_User
0.RootTask_Organization -- 8.BvaDispatchTask_Organization
8.BvaDispatchTask_Organization -- 9.BvaDispatchTask_User
@enduml
```
</details>

![RTO.DTO.ESWTO.SCMTU.JATU.JDRTU.ATU.ARTU-40605](uml/RTO.DTO.ESWTO.SCMTU.JATU.JDRTU.ATU.ARTU-40605.png)

