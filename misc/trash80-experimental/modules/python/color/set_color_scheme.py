class Colors(object):

    def __init__(self):
        self = self
        self.csi = '\033[{0}m'
    #end

#    def 

    pass
#end





# Set the colorscheme
# args: $1 = <scheme number>|<"none">
set_color_scheme()
{
	eval $LOGFS
	local i='' a_script_colors='' a_color_codes=''

	if [[ $1 -ge ${#A_COLOR_SCHEMES[@]} ]];then
		set -- 1
	fi
	# Set a global variable to allow checking for chosen scheme later
	SCHEME="$1"
	if [[ $B_RUNNING_IN_SHELL == 'true' ]];then
		a_color_codes=( $ANSI_COLORS )
	else
		a_color_codes=( $IRC_COLORS )
	fi
	for (( i=0; i < ${#A_COLORS_AVAILABLE[@]}; i++ ))
	do
		eval "${A_COLORS_AVAILABLE[i]}=\"${a_color_codes[i]}\""
	done
	IFS=","
	a_script_colors=( ${A_COLOR_SCHEMES[$1]} )
	IFS="$ORIGINAL_IFS"
	# then assign the colors globally
	C1="${!a_script_colors[0]}"
	C2="${!a_script_colors[1]}"
	CN="${!a_script_colors[2]}"
	# ((COLOR_SCHEME++)) ## note: why is this? ##
	eval $LOGFE
}

"""
http://cia-vc.googlecode.com/svn/trunk/cia/LibCIA/IRC/Formatting.py
http://wiki.bash-hackers.org/scripting/terminalcodes
http://pypi.python.org/pypi/colorama
http://code.google.com/p/colorama/source/browse/colorama/ansi.py
http://pypi.python.org/pypi/termcolor

"""