#
# Conditional build:
%bcond_without	dist_kernel		# without distribution kernel
#
%define		_orig_name	au88xx

Summary:	Aureal Vortex Linux Driver
Summary(pl.UTF-8):	Sterowniki dla Linuksa dla kart dźwiękowych opartych na Aureal Vortex
Name:		kernel-sound-%{_orig_name}
Version:	1.1.2
%define	_rel	16
Release:	%{_rel}@%{_kernel_ver_str}
License:	GPL
Group:		Base/Kernel
Source0:	http://dl.sourceforge.net/aureal/%{_orig_name}-%{version}.tar.bz2
# Source0-md5:	b1aeaa4bb56ac015d90ca5f69261ab84
Patch0:		%{_orig_name}-Makefile.patch
Patch1:		%{name}-types.patch
URL:		http://sourceforge.net/projects/aureal/
%{?with_dist_kernel:BuildRequires:	kernel-headers }
BuildRequires:	rpmbuild(macros) >= 1.118
%{?with_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod
Provides:	au88xx
Obsoletes:	au88xx
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aureal Vortex Linux Driver.

%description -l pl.UTF-8
Sterowniki do kart dźwiękowych opartych na Aureal Vortex.

%package -n kernel-smp-sound-%{_orig_name}
Summary:	Aureal Vortex Linux SMP Driver
Summary(pl.UTF-8):	Sterownik dla Linuksa SMP dla kart dźwiękowych opartych na Aureal Vortex
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_smp}
Requires(post,postun):	/sbin/depmod
Provides:	au88xx
Obsoletes:	au88xx

%description -n kernel-smp-sound-%{_orig_name}
Aureal Vortex Linux SMP Driver.

%description -n kernel-smp-sound-%{_orig_name} -l pl.UTF-8
Sterowniki SMP do kart dźwiękowych opartych na Aureal Vortex.

%prep
%setup -q -n aureal
%patch -P0 -p1
%patch -P1 -p1

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

%clean
rm -rf $RPM_BUILD_ROOT

%post
%depmod %{_kernel_ver}

%postun
%depmod %{_kernel_ver}

%post -n kernel-smp-sound-%{_orig_name}
%depmod %{_kernel_ver}smp

%postun -n kernel-smp-sound-%{_orig_name}
%depmod %{_kernel_ver}smp

%files
%defattr(644,root,root,755)
%doc README ChangeLog
/lib/modules/%{_kernel_ver}/misc/*

%files -n kernel-smp-sound-%{_orig_name}
%defattr(644,root,root,755)
%doc README ChangeLog
/lib/modules/%{_kernel_ver}smp/misc/*
