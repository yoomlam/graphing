| [README.md](/README.md) | [Task Listing](tasklist.md) |

# InformalHearingPresentationTask_User

## Tasks Created Before and After

<details><summary>Tasks created before and after InformalHearingPresentationTask_User</summary>

```
digraph G {
rankdir="LR";
"InformalHearingPresentationTask_User" -> "JudgeAssignTask_User" [label=2]
"InformalHearingPresentationTask_Organization" -> "InformalHearingPresentationTask_User" [label=3]
}
```
</details>

![InformalHearingPresentationTask_User](dot/InformalHearingPresentationTask_User.dot.png)

**Before:**

   * [InformalHearingPresentationTask_Organization](InformalHearingPresentationTask_Organization.md): 3 times

**After:**

   * [JudgeAssignTask_User](JudgeAssignTask_User.md): 2 times

## Task Creation Sequences

### RTO.TVTO.DTO.ESWTO.IHPTO.IHPTU

3 occurrences (example appeal IDs: [15370, 41412, 42019])

<details><summary>Task Tree for appeal with ID 15370</summary>

```
@startuml
skinparam {
  ObjectBorderColor #555
  ObjectBorderThickness 0
  ObjectFontStyle bold
  ObjectFontSize 14
  ObjectAttributeFontColor #333
  ObjectAttributeFontSize 12
}
  object 0.RootTask #66c2a5 {
Organization
}
  object 1.TrackVeteranTask #8da0cb {
Organization
}
  object 2.DistributionTask #fc8d62 {
Organization
}
  object 3.EvidenceSubmissionWindowTask #b3b3b3 {
Organization
}
  object 4.InformalHearingPresentationTask #ffd92f {
Organization
}
  object 5.InformalHearingPresentationTask #ffd92f {
User  <back:white>    </back>
}
  object 6.JudgeAssignTask #8da0cb {
User
}
  object 7.JudgeDecisionReviewTask #66c2a5 {
User
}
  object 8.AttorneyTask #fc8d62 {
User
}
  object 9.BvaDispatchTask #e5c494 {
Organization
}
  object 10.BvaDispatchTask #e5c494 {
User
}
0.RootTask -- 1.TrackVeteranTask
0.RootTask -- 2.DistributionTask
2.DistributionTask -- 3.EvidenceSubmissionWindowTask
2.DistributionTask -- 4.InformalHearingPresentationTask
4.InformalHearingPresentationTask -- 5.InformalHearingPresentationTask
0.RootTask -- 6.JudgeAssignTask
0.RootTask -- 7.JudgeDecisionReviewTask
7.JudgeDecisionReviewTask -- 8.AttorneyTask
0.RootTask -- 9.BvaDispatchTask
9.BvaDispatchTask -- 10.BvaDispatchTask
@enduml
```
</details>

![RTO.TVTO.DTO.ESWTO.IHPTO.IHPTU-15370](uml/RTO.TVTO.DTO.ESWTO.IHPTO.IHPTU-15370.png)

