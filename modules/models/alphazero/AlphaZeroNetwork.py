import torch
import torch.nn as nn

class ConvBlock(nn.Module):
    """
    A block that consists of a convolutional layer, a batch normalization layer,
    and a ReLU activation layer.

    This block is a basic building component in convolutional neural networks.

    :Example:

    >>> conv_block = ConvBlock(3, 64)
    >>> print(conv_block)

    """

    def __init__(self, input_channels, num_filters):
        """
        Initialize the ConvBlock.

        :param input_channels: The number of input channels for the convolutional layer.
        :type input_channels: int
        :param num_filters: The number of filters (or output channels) in the convolutional layer.
        :type num_filters: int
        """
        super().__init__()
        self.conv1 = nn.Conv2d( input_channels, num_filters, 3, padding=1 )
        self.bn1 = nn.BatchNorm2d( num_filters )
        self.relu1 = nn.ReLU()

    def __call__(self, x):
        """
        Apply the convolutional block layers to the input tensor.
    
        This method allows the ConvBlock instance to be used as a callable, applying its
        layers (convolution, batch normalization, and ReLU activation) to the input tensor.
    
        :param x: The input tensor to which the layers will be applied.
        :type x: torch.Tensor
        :return: The output tensor after applying the convolutional block layers.
        :rtype: torch.Tensor
        """
        x = self.conv1( x )
        x = self.bn1( x )
        x = self.relu1( x )

        return x

class ResidualBlock(nn.Module):
    """
    A residual block typically used in ResNet architectures.

    This block is designed to learn residual functions with reference to the layer inputs,
    allowing for the training of deeper neural networks.

    :Example:

    >>> residual_block = ResidualBlock(64)
    >>> print(residual_block)

    """

    def __init__(self, num_filters):
        """
        Initialize the ResidualBlock.

        :param num_filters: The number of filters in the convolutional layers. It is assumed that
                            this is the same as the number of input channels to the block.
        :type num_filters: int
        """
        super().__init__()
        self.conv1 = nn.Conv2d( num_filters, num_filters, 3,
                padding=1 )
        self.bn1 = nn.BatchNorm2d( num_filters )
        self.relu1 = nn.ReLU()
        self.conv2 = nn.Conv2d( num_filters, num_filters, 3,
                padding=1 )
        self.bn2 = nn.BatchNorm2d( num_filters )
        self.relu2 = nn.ReLU()

    def __call__( self, x ):
        """
        Apply the residual block layers to the input tensor.

        :param x: The input tensor to which the residual block layers will be applied.
        :type x: torch.Tensor
        :return: The output tensor after applying the residual block layers and adding the input tensor.
        :rtype: torch.Tensor
        """
        residual = x

        x = self.conv1( x )
        x = self.bn1( x )
        x = self.relu1( x )
        
        x = self.conv2( x )
        x = self.bn2( x )
        x += residual
        x = self.relu2( x )

        return x

class ValueHead(nn.Module):
    """
    A neural network module representing the value head.

    This module is typically used in reinforcement learning models to estimate the value
    of a given state.

    :Example:

    >>> value_head = ValueHead(512)
    >>> print(value_head)

    """

    def __init__(self, input_channels):
        """
        Initialize the ValueHead.

        :param input_channels: The number of input channels to the value head.
        :type input_channels: int
        """
        super().__init__()
        self.conv1 = nn.Conv2d( input_channels, 1, 1 )
        self.bn1 = nn.BatchNorm2d( 1 )
        self.relu1 = nn.ReLU()
        self.fc1 = nn.Linear( 64, 256 )
        self.relu2 = nn.ReLU()
        self.fc2 = nn.Linear( 256, 1 )
        self.tanh1 = nn.Tanh()

    def __call__(self, x):
        """
        Apply the layers of the value head to the input tensor.

        :param x: The input tensor to which the value head layers will be applied.
        :type x: torch.Tensor
        :return: The output tensor after applying the value head layers.
        :rtype: torch.Tensor
        """

        x = self.conv1( x )
        x = self.bn1( x )
        x = self.relu1( x )
        x = x.view( x.shape[0], 64 )
        x = self.fc1( x )
        x = self.relu2( x )
        x = self.fc2( x )
        x = self.tanh1( x )

        return x

class PolicyHead(nn.Module):
    """
    A neural network module representing the policy head.

    This module is typically used in reinforcement learning models to determine the
    policy or action probabilities in a given state.

    :Example:

    >>> policy_head = PolicyHead(512)
    >>> print(policy_head)

    """

    def __init__(self, input_channels):
        """
        Initialize the PolicyHead.

        :param input_channels: The number of input channels to the policy head.
        :type input_channels: int
        """
        super().__init__()
        self.conv1 = nn.Conv2d( input_channels, 2, 1 )
        self.bn1 = nn.BatchNorm2d( 2 )
        self.relu1 = nn.ReLU()
        self.fc1 = nn.Linear( 128, 4608 )
    
    def __call__(self, x):
        """
        Apply the layers of the policy head to the input tensor.

        :param x: The input tensor to which the policy head layers will be applied.
        :type x: torch.Tensor
        :return: The output tensor after applying the policy head layers.
        :rtype: torch.Tensor
        """

        x = self.conv1( x )
        x = self.bn1( x )
        x = self.relu1( x )
        x = x.view( x.shape[0], 128 )
        x = self.fc1( x )

        return x

class AlphaZeroNet(nn.Module):
    """
    A neural network with the AlphaZero architecture.

    This network is designed for use in the AlphaZero algorithm, combining convolutional
    and residual blocks to process game states, with separate value and policy heads for
    evaluating those states and suggesting moves.

    :Example:

    >>> alpha_zero_net = AlphaZeroNet(5, 128)
    >>> print(alpha_zero_net)

    """

    def __init__(self, num_blocks, num_filters):
        """
        Initialize the AlphaZeroNet.

        :param num_blocks: The number of residual blocks in the network.
        :type num_blocks: int
        :param num_filters: The number of filters in each convolutional layer.
        :type num_filters: int
        """
        super().__init__()
        #The number of input planes is fixed at 16
        self.convBlock1 = ConvBlock( 16, num_filters )

        residualBlocks = [ ResidualBlock( num_filters ) for i in range( num_blocks ) ]

        self.residualBlocks = nn.ModuleList( residualBlocks )

        self.valueHead = ValueHead( num_filters )

        self.policyHead = PolicyHead( num_filters )

        self.softmax1 = nn.Softmax( dim=1 )

        self.mseLoss = nn.MSELoss()
        
        self.crossEntropyLoss = nn.CrossEntropyLoss()

    def __call__(self, x, valueTarget=None, policyTarget=None, policyMask=None):
        """
        Apply the AlphaZeroNet to the input tensor, optionally computing loss if targets are provided.

        :param x: The input tensor representing the game state.
        :type x: torch.Tensor
        :param valueTarget: The target value for the game state, used in training.
        :type valueTarget: torch.Tensor, optional
        :param policyTarget: The target policy distribution for the game state, used in training.
        :type policyTarget: torch.Tensor, optional
        :param policyMask: A mask indicating legal moves in the game state, used in training.
        :type policyMask: torch.Tensor, optional
        :return: The output from the value and policy heads, and optionally the loss if targets are provided.
        :rtype: tuple of torch.Tensor, or tuple of torch.Tensor and float
        """

        # Pass input through the initial convolutional block
        x = self.convBlock1(x)

        # Apply each residual block in sequence
        for block in self.residualBlocks:
            x = block(x)

        # Process the output through the value head
        value = self.valueHead(x)

        # Process the output through the policy head
        policy = self.policyHead(x)

        # If in training mode, compute losses
        if self.training:
            # Compute loss for the value head
            valueLoss = self.mseLoss(value, valueTarget)

            # Reshape policy target for loss computation
            policyTarget = policyTarget.view(policyTarget.shape[0])

            # Compute loss for the policy head
            policyLoss = self.crossEntropyLoss(policy, policyTarget)

            return valueLoss, policyLoss

        else:
            # Reshape policy mask for softmax application
            policyMask = policyMask.view(policyMask.shape[0], -1)

            # Apply exponential function to the policy output
            policy_exp = torch.exp(policy)

            # Apply the mask to the policy output
            policy_exp *= policyMask.type(torch.float32)

            # Sum the exponentiated policy outputs
            policy_exp_sum = torch.sum(policy_exp, dim=1, keepdim=True)

            # Normalize the policy output using softmax
            policy_softmax = policy_exp / policy_exp_sum

            return value, policy_softmax
