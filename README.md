## Data-Driven Documentation of Task Trees

Actual task trees were processed and used to generate documentation.

Each task has its own page (i.e., `md` file), see [Task Listing](tasklist.md).
Each task page has the following sections:
* Diagram of inlinks (Backlinks) and outlinks (Nextlinks) to the page. The number on the link represents the number of occurrences where the creation of source task was followed by the creation of the destination task.
* **Nextlinks**: links to tasks that were created _after_ this page's task
* **Backlinks**: links to tasks that were created _before_ this page's task
* Sections of examples grouped according to the sequence of tasks created before this page's task.
  * Section names are formed using acronyms for each task. For example, `RootTask_Organization` is `RTO`. So a section named `RTO.TVTO.DTO.SHTO` means `RootTask_Organization` was created and followed by `TrackVeteranTask_Organization` followed by `DistributionTask_Organization` followed by `ScheduleHearingTask_Organization`. The naming represents the **task creation sequence** (TCS). The last task in the sequence will always refer to this page's task.
  * Each section presents the number of occurrences of that TCS (along with a few appeal IDs that have that TCS) and a task tree diagram of that appeal.
