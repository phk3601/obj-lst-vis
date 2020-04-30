// Generated by gencpp from file object_list/Dimension.msg
// DO NOT EDIT!


#ifndef OBJECT_LIST_MESSAGE_DIMENSION_H
#define OBJECT_LIST_MESSAGE_DIMENSION_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace object_list
{
template <class ContainerAllocator>
struct Dimension_
{
  typedef Dimension_<ContainerAllocator> Type;

  Dimension_()
    : length(0.0)
    , width(0.0)
    , height(0.0)  {
    }
  Dimension_(const ContainerAllocator& _alloc)
    : length(0.0)
    , width(0.0)
    , height(0.0)  {
  (void)_alloc;
    }



   typedef double _length_type;
  _length_type length;

   typedef double _width_type;
  _width_type width;

   typedef double _height_type;
  _height_type height;





  typedef boost::shared_ptr< ::object_list::Dimension_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::object_list::Dimension_<ContainerAllocator> const> ConstPtr;

}; // struct Dimension_

typedef ::object_list::Dimension_<std::allocator<void> > Dimension;

typedef boost::shared_ptr< ::object_list::Dimension > DimensionPtr;
typedef boost::shared_ptr< ::object_list::Dimension const> DimensionConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::object_list::Dimension_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::object_list::Dimension_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::object_list::Dimension_<ContainerAllocator1> & lhs, const ::object_list::Dimension_<ContainerAllocator2> & rhs)
{
  return lhs.length == rhs.length &&
    lhs.width == rhs.width &&
    lhs.height == rhs.height;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::object_list::Dimension_<ContainerAllocator1> & lhs, const ::object_list::Dimension_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace object_list

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::object_list::Dimension_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::object_list::Dimension_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::object_list::Dimension_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::object_list::Dimension_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::object_list::Dimension_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::object_list::Dimension_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::object_list::Dimension_<ContainerAllocator> >
{
  static const char* value()
  {
    return "95f1c31b94fb56f33a669e4bf805939a";
  }

  static const char* value(const ::object_list::Dimension_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x95f1c31b94fb56f3ULL;
  static const uint64_t static_value2 = 0x3a669e4bf805939aULL;
};

template<class ContainerAllocator>
struct DataType< ::object_list::Dimension_<ContainerAllocator> >
{
  static const char* value()
  {
    return "object_list/Dimension";
  }

  static const char* value(const ::object_list::Dimension_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::object_list::Dimension_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 length\n"
"float64 width\n"
"float64 height\n"
;
  }

  static const char* value(const ::object_list::Dimension_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::object_list::Dimension_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.length);
      stream.next(m.width);
      stream.next(m.height);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Dimension_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::object_list::Dimension_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::object_list::Dimension_<ContainerAllocator>& v)
  {
    s << indent << "length: ";
    Printer<double>::stream(s, indent + "  ", v.length);
    s << indent << "width: ";
    Printer<double>::stream(s, indent + "  ", v.width);
    s << indent << "height: ";
    Printer<double>::stream(s, indent + "  ", v.height);
  }
};

} // namespace message_operations
} // namespace ros

#endif // OBJECT_LIST_MESSAGE_DIMENSION_H
