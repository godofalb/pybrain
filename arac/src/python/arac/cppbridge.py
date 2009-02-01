# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.36
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _cppbridge
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


class Buffer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Buffer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Buffer, name)
    def __init__(self, *args, **kwargs): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    def append(*args): return _cppbridge.Buffer_append(*args)
    __swig_destroy__ = _cppbridge.delete_Buffer
    __del__ = lambda self : None;
Buffer_swigregister = _cppbridge.Buffer_swigregister
Buffer_swigregister(Buffer)

class Component(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Component, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Component, name)
    def __init__(self, *args, **kwargs): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    Simple = _cppbridge.Component_Simple
    ErrorAgnostic = _cppbridge.Component_ErrorAgnostic
    Sequential = _cppbridge.Component_Sequential
    SequentialErrorAgnostic = _cppbridge.Component_SequentialErrorAgnostic
    __swig_destroy__ = _cppbridge.delete_Component
    __del__ = lambda self : None;
    def forward(*args): return _cppbridge.Component_forward(*args)
    def backward(*args): return _cppbridge.Component_backward(*args)
    def dry_forward(*args): return _cppbridge.Component_dry_forward(*args)
    def dry_backward(*args): return _cppbridge.Component_dry_backward(*args)
    def set_mode(*args): return _cppbridge.Component_set_mode(*args)
    def clear(*args): return _cppbridge.Component_clear(*args)
    def get_mode(*args): return _cppbridge.Component_get_mode(*args)
    def sequential(*args): return _cppbridge.Component_sequential(*args)
    def timestep(*args): return _cppbridge.Component_timestep(*args)
    def sequencelength(*args): return _cppbridge.Component_sequencelength(*args)
    def error_agnostic(*args): return _cppbridge.Component_error_agnostic(*args)
Component_swigregister = _cppbridge.Component_swigregister
Component_swigregister(Component)

class Module(Component):
    __swig_setmethods__ = {}
    for _s in [Component]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Module, name, value)
    __swig_getmethods__ = {}
    for _s in [Component]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Module, name)
    def __init__(self, *args, **kwargs): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _cppbridge.delete_Module
    __del__ = lambda self : None;
    def forward(*args): return _cppbridge.Module_forward(*args)
    def add_to_input(*args): return _cppbridge.Module_add_to_input(*args)
    def add_to_outerror(*args): return _cppbridge.Module_add_to_outerror(*args)
    def clear(*args): return _cppbridge.Module_clear(*args)
    def input(*args): return _cppbridge.Module_input(*args)
    def output(*args): return _cppbridge.Module_output(*args)
    def inerror(*args): return _cppbridge.Module_inerror(*args)
    def outerror(*args): return _cppbridge.Module_outerror(*args)
    def insize(*args): return _cppbridge.Module_insize(*args)
    def outsize(*args): return _cppbridge.Module_outsize(*args)
    def last_timestep(*args): return _cppbridge.Module_last_timestep(*args)
    def init_input(*args): return _cppbridge.Module_init_input(*args)
    def init_output(*args): return _cppbridge.Module_init_output(*args)
    def init_inerror(*args): return _cppbridge.Module_init_inerror(*args)
    def init_outerror(*args): return _cppbridge.Module_init_outerror(*args)
Module_swigregister = _cppbridge.Module_swigregister
Module_swigregister(Module)

class Parametrized(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Parametrized, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Parametrized, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _cppbridge.new_Parametrized(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cppbridge.delete_Parametrized
    __del__ = lambda self : None;
    def get_parameters(*args): return _cppbridge.Parametrized_get_parameters(*args)
    def set_parameters(*args): return _cppbridge.Parametrized_set_parameters(*args)
    def get_derivatives(*args): return _cppbridge.Parametrized_get_derivatives(*args)
    def set_derivatives(*args): return _cppbridge.Parametrized_set_derivatives(*args)
    def clear_derivatives(*args): return _cppbridge.Parametrized_clear_derivatives(*args)
Parametrized_swigregister = _cppbridge.Parametrized_swigregister
Parametrized_swigregister(Parametrized)

class Connection(Component):
    __swig_setmethods__ = {}
    for _s in [Component]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Connection, name, value)
    __swig_getmethods__ = {}
    for _s in [Component]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Connection, name)
    def __init__(self, *args, **kwargs): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _cppbridge.delete_Connection
    __del__ = lambda self : None;
    def set_incomingstart(*args): return _cppbridge.Connection_set_incomingstart(*args)
    def set_incomingstop(*args): return _cppbridge.Connection_set_incomingstop(*args)
    def set_outgoingstart(*args): return _cppbridge.Connection_set_outgoingstart(*args)
    def set_outgoingstop(*args): return _cppbridge.Connection_set_outgoingstop(*args)
    def get_incomingstart(*args): return _cppbridge.Connection_get_incomingstart(*args)
    def get_incomingstop(*args): return _cppbridge.Connection_get_incomingstop(*args)
    def get_outgoingstart(*args): return _cppbridge.Connection_get_outgoingstart(*args)
    def get_outgoingstop(*args): return _cppbridge.Connection_get_outgoingstop(*args)
    def set_recurrent(*args): return _cppbridge.Connection_set_recurrent(*args)
    def get_recurrent(*args): return _cppbridge.Connection_get_recurrent(*args)
    def incoming(*args): return _cppbridge.Connection_incoming(*args)
    def outgoing(*args): return _cppbridge.Connection_outgoing(*args)
Connection_swigregister = _cppbridge.Connection_swigregister
Connection_swigregister(Connection)

class IdentityConnection(Connection):
    __swig_setmethods__ = {}
    for _s in [Connection]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, IdentityConnection, name, value)
    __swig_getmethods__ = {}
    for _s in [Connection]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, IdentityConnection, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _cppbridge.new_IdentityConnection(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cppbridge.delete_IdentityConnection
    __del__ = lambda self : None;
IdentityConnection_swigregister = _cppbridge.IdentityConnection_swigregister
IdentityConnection_swigregister(IdentityConnection)

class Bias(Module):
    __swig_setmethods__ = {}
    for _s in [Module]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Bias, name, value)
    __swig_getmethods__ = {}
    for _s in [Module]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Bias, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _cppbridge.new_Bias(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cppbridge.delete_Bias
    __del__ = lambda self : None;
Bias_swigregister = _cppbridge.Bias_swigregister
Bias_swigregister(Bias)

class GateLayer(Module):
    __swig_setmethods__ = {}
    for _s in [Module]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GateLayer, name, value)
    __swig_getmethods__ = {}
    for _s in [Module]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, GateLayer, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _cppbridge.new_GateLayer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cppbridge.delete_GateLayer
    __del__ = lambda self : None;
GateLayer_swigregister = _cppbridge.GateLayer_swigregister
GateLayer_swigregister(GateLayer)

class LinearLayer(Module):
    __swig_setmethods__ = {}
    for _s in [Module]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, LinearLayer, name, value)
    __swig_getmethods__ = {}
    for _s in [Module]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, LinearLayer, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _cppbridge.new_LinearLayer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cppbridge.delete_LinearLayer
    __del__ = lambda self : None;
LinearLayer_swigregister = _cppbridge.LinearLayer_swigregister
LinearLayer_swigregister(LinearLayer)

class LstmLayer(Module):
    __swig_setmethods__ = {}
    for _s in [Module]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, LstmLayer, name, value)
    __swig_getmethods__ = {}
    for _s in [Module]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, LstmLayer, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _cppbridge.new_LstmLayer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cppbridge.delete_LstmLayer
    __del__ = lambda self : None;
    def init_state(*args): return _cppbridge.LstmLayer_init_state(*args)
    def init_state_error(*args): return _cppbridge.LstmLayer_init_state_error(*args)
LstmLayer_swigregister = _cppbridge.LstmLayer_swigregister
LstmLayer_swigregister(LstmLayer)

class MdlstmLayer(Module):
    __swig_setmethods__ = {}
    for _s in [Module]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, MdlstmLayer, name, value)
    __swig_getmethods__ = {}
    for _s in [Module]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, MdlstmLayer, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _cppbridge.new_MdlstmLayer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cppbridge.delete_MdlstmLayer
    __del__ = lambda self : None;
MdlstmLayer_swigregister = _cppbridge.MdlstmLayer_swigregister
MdlstmLayer_swigregister(MdlstmLayer)

class PartialSoftmaxLayer(Module):
    __swig_setmethods__ = {}
    for _s in [Module]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, PartialSoftmaxLayer, name, value)
    __swig_getmethods__ = {}
    for _s in [Module]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, PartialSoftmaxLayer, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _cppbridge.new_PartialSoftmaxLayer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cppbridge.delete_PartialSoftmaxLayer
    __del__ = lambda self : None;
PartialSoftmaxLayer_swigregister = _cppbridge.PartialSoftmaxLayer_swigregister
PartialSoftmaxLayer_swigregister(PartialSoftmaxLayer)

class SigmoidLayer(Module):
    __swig_setmethods__ = {}
    for _s in [Module]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SigmoidLayer, name, value)
    __swig_getmethods__ = {}
    for _s in [Module]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, SigmoidLayer, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _cppbridge.new_SigmoidLayer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cppbridge.delete_SigmoidLayer
    __del__ = lambda self : None;
SigmoidLayer_swigregister = _cppbridge.SigmoidLayer_swigregister
SigmoidLayer_swigregister(SigmoidLayer)

class SoftmaxLayer(Module):
    __swig_setmethods__ = {}
    for _s in [Module]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SoftmaxLayer, name, value)
    __swig_getmethods__ = {}
    for _s in [Module]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, SoftmaxLayer, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _cppbridge.new_SoftmaxLayer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cppbridge.delete_SoftmaxLayer
    __del__ = lambda self : None;
SoftmaxLayer_swigregister = _cppbridge.SoftmaxLayer_swigregister
SoftmaxLayer_swigregister(SoftmaxLayer)

class TanhLayer(Module):
    __swig_setmethods__ = {}
    for _s in [Module]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, TanhLayer, name, value)
    __swig_getmethods__ = {}
    for _s in [Module]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, TanhLayer, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _cppbridge.new_TanhLayer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cppbridge.delete_TanhLayer
    __del__ = lambda self : None;
TanhLayer_swigregister = _cppbridge.TanhLayer_swigregister
TanhLayer_swigregister(TanhLayer)

class BaseNetwork(Module):
    __swig_setmethods__ = {}
    for _s in [Module]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, BaseNetwork, name, value)
    __swig_getmethods__ = {}
    for _s in [Module]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, BaseNetwork, name)
    def __init__(self, *args, **kwargs): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _cppbridge.delete_BaseNetwork
    __del__ = lambda self : None;
    def activate(*args): return _cppbridge.BaseNetwork_activate(*args)
    def back_activate(*args): return _cppbridge.BaseNetwork_back_activate(*args)
    def forward(*args): return _cppbridge.BaseNetwork_forward(*args)
BaseNetwork_swigregister = _cppbridge.BaseNetwork_swigregister
BaseNetwork_swigregister(BaseNetwork)

class FullConnection(Connection,Parametrized):
    __swig_setmethods__ = {}
    for _s in [Connection,Parametrized]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, FullConnection, name, value)
    __swig_getmethods__ = {}
    for _s in [Connection,Parametrized]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, FullConnection, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _cppbridge.delete_FullConnection
    __del__ = lambda self : None;
    def __init__(self, *args): 
        this = _cppbridge.new_FullConnection(*args)
        try: self.this.append(this)
        except: self.this = this
FullConnection_swigregister = _cppbridge.FullConnection_swigregister
FullConnection_swigregister(FullConnection)

class LinearConnection(Connection,Parametrized):
    __swig_setmethods__ = {}
    for _s in [Connection,Parametrized]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, LinearConnection, name, value)
    __swig_getmethods__ = {}
    for _s in [Connection,Parametrized]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, LinearConnection, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _cppbridge.delete_LinearConnection
    __del__ = lambda self : None;
    def __init__(self, *args): 
        this = _cppbridge.new_LinearConnection(*args)
        try: self.this.append(this)
        except: self.this = this
LinearConnection_swigregister = _cppbridge.LinearConnection_swigregister
LinearConnection_swigregister(LinearConnection)

class Network(BaseNetwork):
    __swig_setmethods__ = {}
    for _s in [BaseNetwork]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Network, name, value)
    __swig_getmethods__ = {}
    for _s in [BaseNetwork]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Network, name)
    __repr__ = _swig_repr
    Simple = _cppbridge.Network_Simple
    InputModule = _cppbridge.Network_InputModule
    OutputModule = _cppbridge.Network_OutputModule
    InputOutputModule = _cppbridge.Network_InputOutputModule
    def __init__(self, *args): 
        this = _cppbridge.new_Network(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _cppbridge.delete_Network
    __del__ = lambda self : None;
    def clear(*args): return _cppbridge.Network_clear(*args)
    def add_module(*args): return _cppbridge.Network_add_module(*args)
    def add_connection(*args): return _cppbridge.Network_add_connection(*args)
    def activate(*args): return _cppbridge.Network_activate(*args)
    def back_activate(*args): return _cppbridge.Network_back_activate(*args)
Network_swigregister = _cppbridge.Network_swigregister
Network_swigregister(Network)


