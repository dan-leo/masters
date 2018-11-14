/*
 * AUTO-GENERATED _componentMain.c for the cpuproc component.

 * Don't bother hand-editing this file.
 */

#include "legato.h"
#include "../liblegato/eventLoop.h"
#include "../liblegato/log.h"

#ifdef __cplusplus
extern "C" {
#endif

// Component log session variables.
le_log_SessionRef_t cpuproc_LogSession;
le_log_Level_t* cpuproc_LogLevelFilterPtr;

// Component initialization function (COMPONENT_INIT).
void _cpuproc_COMPONENT_INIT(void);

// Library initialization function.
// Will be called by the dynamic linker loader when the library is loaded.
__attribute__((constructor)) void _cpuproc_Init(void)
{
    LE_DEBUG("Initializing cpuproc component library.");

    // Register the component with the Log Daemon.
    cpuproc_LogSession = log_RegComponent("cpuproc", &cpuproc_LogLevelFilterPtr);

    //Queue the COMPONENT_INIT function to be called by the event loop
    event_QueueComponentInit(_cpuproc_COMPONENT_INIT);
}


#ifdef __cplusplus
}
#endif
