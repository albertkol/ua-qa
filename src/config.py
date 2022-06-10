TITLE = """
                 ,---,                     ,----..        ,---, 
         ,--,   '  .' \                   /   /   \      '  .' \ 
       ,'_ /|  /  ;    '.        ,---,.  /   .     :    /  ;    '. 
  .--. |  | : :  :       \     ,'  .' | .   /   ;.  \  :  :       \ 
,'_ /| :  . | :  |   /\   \  ,---.'   ,.   ;   /  ` ;  :  |   /\   \ 
|  ' | |  . . |  :  ' ;.   : |   |    |;   |  ; \ ; |  |  :  ' ;.   : 
|  | ' |  | | |  |  ;/  \   \:   :  .' |   :  | ; | '  |  |  ;/  \   \ 
:  | | :  ' ; '  :  | \  \ ,':   |.'   .   |  ' ' ' :  '  :  | \  \ ,' 
|  ; ' |  | ' |  |  '  '--'  `---'     '   ;  \; /  |  |  |  '  '--' 
:  | : ;  ; | |  :  :                   \   \  ',  . \ |  :  : 
'  :  `--'   \|  | ,'                    ;   :      ; ||  | ,' 
:  ,      .-./`--''                       \   \ .'`--" `--'' 
 `--`----'                                 `---` 


----------------------------------------------------

Welcome!

----------------------------------------------------

UA QA tool was designed with the goal to make 
difficult UA QA scenarios a child's play.

Tool options:
    - login                 SSO login
    - use                   Set user you want to work on
    - attach offer          Attach offer to user in use
    - attach renewal        Attach renewal to user in use
    - clear                 Clear user in use accounts
    - exit                  Close ua-qa tool

Let's start with the QA...
"""  # noqa: W605 W291

CRED = "\033[91m"
CGREEN = "\33[32m"
CYELLOW = "\33[33m"
CBLUE = "\33[34m"
CGREY = "\33[90m"
CEND = "\033[0m"
CONTRACTS_BIN = "/go/bin/contract"

COMMANDS = [
    "login",
    "status",
    "use",
    "attach renewal",
    "attach renewal --expired",
    "attach renewal --no-actionable",
    "attach renewal --multi",
    "attach offer",
    "attach offer --multi",
    "clear",
    "exit",
]
