
# conditional build
# _without_dist_kernel          without distribution kernel

#%define		__kernel_ver	%(grep UTS_RELEASE %{_kernelsrcdir}/include/linux/version.h 2>/dev/null | cut -d'"' -f2)
#%define		__kernel_rel	%(rpm -qf %{_kernelsrcdir}/include/linux/version.h --queryformat "%{RELEASE}" | grep -v "is not")
#%define		_kernel_ver	%(echo %{__kernel_ver}%{!?_without_dist_kernel:-%{__kernel_rel}})
#%define		_kernel_ver_str	%(echo %{_kernel_ver} | sed s/-/_/g)
%define		_orig_name	au88xx
%define		_rel 5

Summary:	Aureal Vortex Linux Driver
Summary(pl):	Sterowniki dla Linuxa dla kart d德i瘯owych opartych na Aureal Vortex
Name:		kernel-sound-%{_orig_name}
Version:	1.1.2
Release:	%{_rel}@%{_kernel_ver_str}
License:	GPL
Group:		Base/Kernel
Source0:	http://prdownloads.sourceforge.net/aureal/%{_orig_name}-%{version}.tar.bz2
Patch0:		%{_orig_name}-Makefile.patch
%{!?_without_dist_kernel:BuildRequires:         kernel-headers }
Prereq:		/sbin/depmod
%{!?_without_dist_kernel:%requires_releq_kernel_up}
Provides:	au88xx
Obsoletes:	au88xx
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aureal Vortex Linux Driver.

%description -l pl
Sterowniki do kart d德i瘯owych opartych na Aureal Vortex.

%package -n kernel-smp-sound-%{_orig_name}
Summary:	Aureal Vortex Linux SMP Driver
Summary(pl):	Sterownik dla Linuxa SMP dla kart d德i瘯owych opartych na Aureal Vortex
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Prereq:		/sbin/depmod
%{!?_without_dist_kernel:%requires_releq_kernel_smp}
Provides:	au88xx
Obsoletes:	au88xx

%description -n kernel-smp-sound-%{_orig_name}
Aureal Vortex Linux SMP Driver.

%description -n kernel-smp-sound-%{_orig_name} -l pl
Sterowniki SMP do kart d德i瘯owych opartych na Aureal Vortex.

%prep
%setup -q -n aureal
%patch0 -p1

%build
#8810
%{__make} CFLAGS="-D__KERNEL__ -D__SMP__ -D__KERNEL_SMP=1 -DMODULE -DAU8810 %{rpmcflags} -fomit-frame-pointer -pipe -Wall -I%{_kernelsrcdir}/include" AUCHIP=AU8810 au8810.o
mv -f au8810.o au8810-smp.o
%{__make} clean
%{__make} CFLAGS="-D__KERNEL__ -DMODULE -DAU8810 %{rpmcflags} -fomit-frame-pointer -pipe -Wall -I%{_kernelsrcdir}/include" AUCHIP=AU8810 au8810.o
%{__make} clean

#8820
%{__make} CFLAGS="-D__KERNEL__ -D__SMP__ -D__KERNEL_SMP=1 -DMODULE -DAU8820 %{rpmcflags} -fomit-frame-pointer -pipe -Wall -I%{_kernelsrcdir}/include" AUCHIP=AU8820 au8820.o
mv -f au8820.o au8820-smp.o
%{__make} clean
%{__make} CFLAGS="-D__KERNEL__ -DMODULE -DAU8820 %{rpmcflags} -fomit-frame-pointer -pipe -Wall -I%{_kernelsrcdir}/include" AUCHIP=AU8820 au8820.o
%{__make} clean

#8830
%{__make} CFLAGS="-D__KERNEL__ -D__SMP__ -D__KERNEL_SMP=1 -DMODULE -DAU8830 %{rpmcflags} -fomit-frame-pointer -pipe -Wall -I%{_kernelsrcdir}/include" AUCHIP=AU8830 au8830.o
mv -f au8830.o au8830-smp.o
%{__make} clean
%{__make} CFLAGS="-D__KERNEL__ -DMODULE -DAU8830 %{rpmcflags} -fomit-frame-pointer -pipe -Wall -I%{_kernelsrcdir}/include" AUCHIP=AU8830 au8830.o

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc
install -d $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/misc
#8810
install au8810-smp.o $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/misc/au8810.o
install au8810.o $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc/au8810.o
#8820
install au8820-smp.o $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/misc/au8820.o
install au8820.o $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc/au8820.o
#8830
install au8830-smp.o $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/misc/au8830.o
install au8830.o $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc/au8830.o

gzip -9nf README ChangeLog

%clean 
rm -rf $RPM_BUILD_ROOT

%post
/sbin/depmod -a

%postun
/sbin/depmod -a

%post -n kernel-smp-sound-%{_orig_name}
/sbin/depmod -a

%postun -n kernel-smp-sound-%{_orig_name}
/sbin/depmod -a

%files
%defattr(644,root,root,755)
%doc *.gz
/lib/modules/%{_kernel_ver}/misc/*

%files -n kernel-smp-sound-%{_orig_name}
%defattr(644,root,root,755)
%doc *.gz 
/lib/modules/%{_kernel_ver}smp/misc/*
