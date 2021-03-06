template_string = '''#!/bin/bash

#PBS -S /bin/bash
#PBS -N ${jobname}
#PBS -m n
#PBS -k eo
#PBS -l walltime=$walltime
#PBS -o ${submit_script_dir}/${jobname}.submit.stdout
#PBS -e ${submit_script_dir}/${jobname}.submit.stderr
#PBS -v WORKER_LOGGING_LEVEL
${overrides}

export JOBNAME="${jobname}"

${user_script}

'''
