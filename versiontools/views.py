from django.shortcuts import render, render_to_response
from versiontools.osutils import AssemblyInfoFinder
from django.template.context import RequestContext

# Create your views here.
def show_assemblyinfo(request):
    af = AssemblyInfoFinder()
    directory_to_scan =r'C:\Users\lberrocal\Documents\Visual Studio 2010\Projects\vessel_scheling_app'
    af.find(directory_to_scan)
    
    context = RequestContext(request)
    
    context_dict = {'assembly_info_list': af.assembly_info_list,
                    'scanned_directory' : directory_to_scan,
                    'dlen'              : 30}

    return render_to_response('versiontools/assembly-info-list.html', context_dict, context)
    
    