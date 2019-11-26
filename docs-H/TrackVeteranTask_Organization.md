| [README.md](/README.md) | [Task Listing](tasklist.md) |

# TrackVeteranTask_Organization

[TrackVeteranTask_Organization description](../descr/TrackVeteranTask_Organization.md)

## Tasks Created Before and After

<details><summary>Tasks created before and after TrackVeteranTask_Organization</summary>

```
digraph G {
rankdir="LR";
"RootTask_Organization" -> "TrackVeteranTask_Organization" [label=120]
"TrackVeteranTask_Organization" -> "DistributionTask_Organization" [label=120]
"HearingTask_Organization" -> "TrackVeteranTask_Organization" [label=1]
}
```
</details>

![TrackVeteranTask_Organization](dot/TrackVeteranTask_Organization.dot.png)

**Before:**

   * [RootTask_Organization](RootTask_Organization.md): 120 times
   * [HearingTask_Organization](HearingTask_Organization.md): 1 times

**After:**

   * [DistributionTask_Organization](DistributionTask_Organization.md): 120 times

## Task Creation Sequences

### RTO.TVTO

[RTO.TVTO description](../descr/RTO.TVTO.md)

120 occurrences (example appeal IDs: [16461, 42769, 42820, 42010, 42071])

<details><summary>Task Tree for appeal with ID 16461</summary>

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
Organization  <back:white>    </back>
}
  object 2.DistributionTask #fc8d62 {
Organization
}
  object 3.ScheduleHearingTask #a6d854 {
Organization
}
  object 4.HearingTask #e78ac3 {
Organization
}
0.RootTask -- 1.TrackVeteranTask
0.RootTask -- 2.DistributionTask
4.HearingTask -- 3.ScheduleHearingTask
2.DistributionTask -- 4.HearingTask
@enduml
```
</details>

![RTO.TVTO-16461](uml/RTO.TVTO-16461.png)

### RTO.DTO.SHTO.HTO.TVTO

[RTO.DTO.SHTO.HTO.TVTO description](../descr/RTO.DTO.SHTO.HTO.TVTO.md)

1 occurrences (example appeal IDs: [4988])

<details><summary>Task Tree for appeal with ID 4988</summary>

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
  object 1.DistributionTask #fc8d62 {
Organization
}
  object 2.ScheduleHearingTask #a6d854 {
Organization
}
  object 3.HearingTask #e78ac3 {
Organization
}
  object 4.TrackVeteranTask #8da0cb {
Organization  <back:white>    </back>
}
0.RootTask -- 1.DistributionTask
3.HearingTask -- 2.ScheduleHearingTask
1.DistributionTask -- 3.HearingTask
0.RootTask -- 4.TrackVeteranTask
@enduml
```
</details>

![RTO.DTO.SHTO.HTO.TVTO-4988](uml/RTO.DTO.SHTO.HTO.TVTO-4988.png)

