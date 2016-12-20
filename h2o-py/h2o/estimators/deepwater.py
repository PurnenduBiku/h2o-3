#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from __future__ import absolute_import, division, print_function, unicode_literals

from h2o.estimators.estimator_base import H2OEstimator
from h2o.exceptions import H2OValueError
from h2o.frame import H2OFrame
from h2o.utils.typechecks import assert_is_type, Enum, numeric
import h2o


class H2ODeepWaterEstimator(H2OEstimator):
    """
    Deep Water

    Build a Deep Learning model using multiple native GPU backends
    Builds a deep neural network on an H2OFrame containing various data sources
    """

    algo = "deepwater"

    def __init__(self, **kwargs):
        super(H2ODeepWaterEstimator, self).__init__()
        self._parms = {}
        names_list = {"model_id", "checkpoint", "autoencoder", "training_frame", "validation_frame", "nfolds",
                      "balance_classes", "max_after_balance_size", "class_sampling_factors",
                      "keep_cross_validation_predictions", "keep_cross_validation_fold_assignment", "fold_assignment",
                      "fold_column", "response_column", "offset_column", "weights_column", "ignored_columns",
                      "score_each_iteration", "categorical_encoding", "overwrite_with_best_model", "epochs",
                      "train_samples_per_iteration", "target_ratio_comm_to_comp", "seed", "standardize",
                      "learning_rate", "learning_rate_annealing", "momentum_start", "momentum_ramp", "momentum_stable",
                      "distribution", "score_interval", "score_training_samples", "score_validation_samples",
                      "score_duty_cycle", "classification_stop", "regression_stop", "stopping_rounds",
                      "stopping_metric", "stopping_tolerance", "max_runtime_secs", "ignore_const_cols",
                      "shuffle_training_data", "mini_batch_size", "clip_gradient", "network", "backend", "image_shape",
                      "channels", "sparse", "gpu", "device_id", "network_definition_file", "network_parameters_file",
                      "mean_image_file", "export_native_parameters_prefix", "activation", "hidden",
                      "input_dropout_ratio", "hidden_dropout_ratios", "problem_type"}
        if "Lambda" in kwargs: kwargs["lambda_"] = kwargs.pop("Lambda")
        for pname, pvalue in kwargs.items():
            if pname == 'model_id':
                self._id = pvalue
                self._parms["model_id"] = pvalue
            elif pname in names_list:
                # Using setattr(...) will invoke type-checking of the arguments
                setattr(self, pname, pvalue)
            else:
                raise H2OValueError("Unknown parameter %s = %r" % (pname, pvalue))

    @property
    def checkpoint(self):
        """str: Model checkpoint to resume training with."""
        return self._parms.get("checkpoint")

    @checkpoint.setter
    def checkpoint(self, checkpoint):
        assert_is_type(checkpoint, None, str, H2OEstimator)
        self._parms["checkpoint"] = checkpoint


    @property
    def autoencoder(self):
        """bool: Auto-Encoder. (Default: False)"""
        return self._parms.get("autoencoder")

    @autoencoder.setter
    def autoencoder(self, autoencoder):
        assert_is_type(autoencoder, None, bool)
        self._parms["autoencoder"] = autoencoder


    @property
    def training_frame(self):
        """str: Id of the training data frame (Not required, to allow initial validation of model parameters)."""
        return self._parms.get("training_frame")

    @training_frame.setter
    def training_frame(self, training_frame):
        assert_is_type(training_frame, None, H2OFrame)
        self._parms["training_frame"] = training_frame


    @property
    def validation_frame(self):
        """str: Id of the validation data frame."""
        return self._parms.get("validation_frame")

    @validation_frame.setter
    def validation_frame(self, validation_frame):
        assert_is_type(validation_frame, None, H2OFrame)
        self._parms["validation_frame"] = validation_frame


    @property
    def nfolds(self):
        """int: Number of folds for N-fold cross-validation (0 to disable or >= 2). (Default: 0)"""
        return self._parms.get("nfolds")

    @nfolds.setter
    def nfolds(self, nfolds):
        assert_is_type(nfolds, None, int)
        self._parms["nfolds"] = nfolds


    @property
    def balance_classes(self):
        """
        bool: Balance training data class counts via over/under-sampling (for imbalanced data). (Default: False)
        """
        return self._parms.get("balance_classes")

    @balance_classes.setter
    def balance_classes(self, balance_classes):
        assert_is_type(balance_classes, None, bool)
        self._parms["balance_classes"] = balance_classes


    @property
    def max_after_balance_size(self):
        """
        float: Maximum relative size of the training data after balancing class counts (can be less than 1.0). Requires
        balance_classes. (Default: 5)
        """
        return self._parms.get("max_after_balance_size")

    @max_after_balance_size.setter
    def max_after_balance_size(self, max_after_balance_size):
        assert_is_type(max_after_balance_size, None, float)
        self._parms["max_after_balance_size"] = max_after_balance_size


    @property
    def class_sampling_factors(self):
        """
        List[float]: Desired over/under-sampling ratios per class (in lexicographic order). If not specified, sampling
        factors will be automatically computed to obtain class balance during training. Requires balance_classes.
        """
        return self._parms.get("class_sampling_factors")

    @class_sampling_factors.setter
    def class_sampling_factors(self, class_sampling_factors):
        assert_is_type(class_sampling_factors, None, [float])
        self._parms["class_sampling_factors"] = class_sampling_factors


    @property
    def keep_cross_validation_predictions(self):
        """bool: Whether to keep the predictions of the cross-validation models. (Default: False)"""
        return self._parms.get("keep_cross_validation_predictions")

    @keep_cross_validation_predictions.setter
    def keep_cross_validation_predictions(self, keep_cross_validation_predictions):
        assert_is_type(keep_cross_validation_predictions, None, bool)
        self._parms["keep_cross_validation_predictions"] = keep_cross_validation_predictions


    @property
    def keep_cross_validation_fold_assignment(self):
        """bool: Whether to keep the cross-validation fold assignment. (Default: False)"""
        return self._parms.get("keep_cross_validation_fold_assignment")

    @keep_cross_validation_fold_assignment.setter
    def keep_cross_validation_fold_assignment(self, keep_cross_validation_fold_assignment):
        assert_is_type(keep_cross_validation_fold_assignment, None, bool)
        self._parms["keep_cross_validation_fold_assignment"] = keep_cross_validation_fold_assignment


    @property
    def fold_assignment(self):
        """
        Enum["auto", "random", "modulo", "stratified"]: Cross-validation fold assignment scheme, if fold_column is not
        specified. The 'Stratified' option will stratify the folds based on the response variable, for classification
        problems. (Default: "auto")
        """
        return self._parms.get("fold_assignment")

    @fold_assignment.setter
    def fold_assignment(self, fold_assignment):
        assert_is_type(fold_assignment, None, Enum("auto", "random", "modulo", "stratified"))
        self._parms["fold_assignment"] = fold_assignment


    @property
    def fold_column(self):
        """str: Column with cross-validation fold index assignment per observation."""
        return self._parms.get("fold_column")

    @fold_column.setter
    def fold_column(self, fold_column):
        assert_is_type(fold_column, None, str)
        self._parms["fold_column"] = fold_column


    @property
    def response_column(self):
        """str: Response variable column."""
        return self._parms.get("response_column")

    @response_column.setter
    def response_column(self, response_column):
        assert_is_type(response_column, None, str)
        self._parms["response_column"] = response_column


    @property
    def offset_column(self):
        """
        str: Offset column. This will be added to the combination of columns before applying the link function.
        """
        return self._parms.get("offset_column")

    @offset_column.setter
    def offset_column(self, offset_column):
        assert_is_type(offset_column, None, str)
        self._parms["offset_column"] = offset_column


    @property
    def weights_column(self):
        """
        str: Column with observation weights. Giving some observation a weight of zero is equivalent to excluding it
        from the dataset; giving an observation a relative weight of 2 is equivalent to repeating that row twice.
        Negative weights are not allowed.
        """
        return self._parms.get("weights_column")

    @weights_column.setter
    def weights_column(self, weights_column):
        assert_is_type(weights_column, None, str)
        self._parms["weights_column"] = weights_column


    @property
    def ignored_columns(self):
        """List[str]: Names of columns to ignore for training."""
        return self._parms.get("ignored_columns")

    @ignored_columns.setter
    def ignored_columns(self, ignored_columns):
        assert_is_type(ignored_columns, None, [str])
        self._parms["ignored_columns"] = ignored_columns


    @property
    def score_each_iteration(self):
        """bool: Whether to score during each iteration of model training. (Default: False)"""
        return self._parms.get("score_each_iteration")

    @score_each_iteration.setter
    def score_each_iteration(self, score_each_iteration):
        assert_is_type(score_each_iteration, None, bool)
        self._parms["score_each_iteration"] = score_each_iteration


    @property
    def categorical_encoding(self):
        """
        Enum["auto", "enum", "one_hot_internal", "one_hot_explicit", "binary", "eigen"]: Encoding scheme for categorical
        features (Default: "auto")
        """
        return self._parms.get("categorical_encoding")

    @categorical_encoding.setter
    def categorical_encoding(self, categorical_encoding):
        assert_is_type(categorical_encoding, None, Enum("auto", "enum", "one_hot_internal", "one_hot_explicit", "binary", "eigen"))
        self._parms["categorical_encoding"] = categorical_encoding


    @property
    def overwrite_with_best_model(self):
        """
        bool: If enabled, override the final model with the best model found during training. (Default: True)
        """
        return self._parms.get("overwrite_with_best_model")

    @overwrite_with_best_model.setter
    def overwrite_with_best_model(self, overwrite_with_best_model):
        assert_is_type(overwrite_with_best_model, None, bool)
        self._parms["overwrite_with_best_model"] = overwrite_with_best_model


    @property
    def epochs(self):
        """float: How many times the dataset should be iterated (streamed), can be fractional. (Default: 10)"""
        return self._parms.get("epochs")

    @epochs.setter
    def epochs(self, epochs):
        assert_is_type(epochs, None, numeric)
        self._parms["epochs"] = epochs


    @property
    def train_samples_per_iteration(self):
        """
        int: Number of training samples (globally) per MapReduce iteration. Special values are 0: one epoch, -1: all
        available data (e.g., replicated training data), -2: automatic. (Default: -2)
        """
        return self._parms.get("train_samples_per_iteration")

    @train_samples_per_iteration.setter
    def train_samples_per_iteration(self, train_samples_per_iteration):
        assert_is_type(train_samples_per_iteration, None, int)
        self._parms["train_samples_per_iteration"] = train_samples_per_iteration


    @property
    def target_ratio_comm_to_comp(self):
        """
        float: Target ratio of communication overhead to computation. Only for multi-node operation and
        train_samples_per_iteration = -2 (auto-tuning). (Default: 0.05)
        """
        return self._parms.get("target_ratio_comm_to_comp")

    @target_ratio_comm_to_comp.setter
    def target_ratio_comm_to_comp(self, target_ratio_comm_to_comp):
        assert_is_type(target_ratio_comm_to_comp, None, numeric)
        self._parms["target_ratio_comm_to_comp"] = target_ratio_comm_to_comp


    @property
    def seed(self):
        """
        int: Seed for random numbers (affects sampling) - Note: only reproducible when running single threaded.
        (Default: -1)
        """
        return self._parms.get("seed")

    @seed.setter
    def seed(self, seed):
        assert_is_type(seed, None, int)
        self._parms["seed"] = seed


    @property
    def standardize(self):
        """
        bool: If enabled, automatically standardize the data. If disabled, the user must provide properly scaled input
        data. (Default: True)
        """
        return self._parms.get("standardize")

    @standardize.setter
    def standardize(self, standardize):
        assert_is_type(standardize, None, bool)
        self._parms["standardize"] = standardize


    @property
    def learning_rate(self):
        """float: Learning rate (higher => less stable, lower => slower convergence). (Default: 0.005)"""
        return self._parms.get("learning_rate")

    @learning_rate.setter
    def learning_rate(self, learning_rate):
        assert_is_type(learning_rate, None, numeric)
        self._parms["learning_rate"] = learning_rate


    @property
    def learning_rate_annealing(self):
        """float: Learning rate annealing: rate / (1 + rate_annealing * samples). (Default: 1e-06)"""
        return self._parms.get("learning_rate_annealing")

    @learning_rate_annealing.setter
    def learning_rate_annealing(self, learning_rate_annealing):
        assert_is_type(learning_rate_annealing, None, numeric)
        self._parms["learning_rate_annealing"] = learning_rate_annealing


    @property
    def momentum_start(self):
        """float: Initial momentum at the beginning of training (try 0.5). (Default: 0.9)"""
        return self._parms.get("momentum_start")

    @momentum_start.setter
    def momentum_start(self, momentum_start):
        assert_is_type(momentum_start, None, numeric)
        self._parms["momentum_start"] = momentum_start


    @property
    def momentum_ramp(self):
        """float: Number of training samples for which momentum increases. (Default: 10000)"""
        return self._parms.get("momentum_ramp")

    @momentum_ramp.setter
    def momentum_ramp(self, momentum_ramp):
        assert_is_type(momentum_ramp, None, numeric)
        self._parms["momentum_ramp"] = momentum_ramp


    @property
    def momentum_stable(self):
        """float: Final momentum after the ramp is over (try 0.99). (Default: 0.99)"""
        return self._parms.get("momentum_stable")

    @momentum_stable.setter
    def momentum_stable(self, momentum_stable):
        assert_is_type(momentum_stable, None, numeric)
        self._parms["momentum_stable"] = momentum_stable


    @property
    def distribution(self):
        """
        Enum["auto", "bernoulli", "multinomial", "gaussian", "poisson", "gamma", "tweedie", "laplace", "quantile",
        "huber"]: Distribution function (Default: "auto")
        """
        return self._parms.get("distribution")

    @distribution.setter
    def distribution(self, distribution):
        assert_is_type(distribution, None, Enum("auto", "bernoulli", "multinomial", "gaussian", "poisson", "gamma", "tweedie", "laplace", "quantile", "huber"))
        self._parms["distribution"] = distribution


    @property
    def score_interval(self):
        """float: Shortest time interval (in seconds) between model scoring. (Default: 5)"""
        return self._parms.get("score_interval")

    @score_interval.setter
    def score_interval(self, score_interval):
        assert_is_type(score_interval, None, numeric)
        self._parms["score_interval"] = score_interval


    @property
    def score_training_samples(self):
        """int: Number of training set samples for scoring (0 for all). (Default: 10000)"""
        return self._parms.get("score_training_samples")

    @score_training_samples.setter
    def score_training_samples(self, score_training_samples):
        assert_is_type(score_training_samples, None, int)
        self._parms["score_training_samples"] = score_training_samples


    @property
    def score_validation_samples(self):
        """int: Number of validation set samples for scoring (0 for all). (Default: 0)"""
        return self._parms.get("score_validation_samples")

    @score_validation_samples.setter
    def score_validation_samples(self, score_validation_samples):
        assert_is_type(score_validation_samples, None, int)
        self._parms["score_validation_samples"] = score_validation_samples


    @property
    def score_duty_cycle(self):
        """
        float: Maximum duty cycle fraction for scoring (lower: more training, higher: more scoring). (Default: 0.1)
        """
        return self._parms.get("score_duty_cycle")

    @score_duty_cycle.setter
    def score_duty_cycle(self, score_duty_cycle):
        assert_is_type(score_duty_cycle, None, numeric)
        self._parms["score_duty_cycle"] = score_duty_cycle


    @property
    def classification_stop(self):
        """
        float: Stopping criterion for classification error fraction on training data (-1 to disable). (Default: 0)
        """
        return self._parms.get("classification_stop")

    @classification_stop.setter
    def classification_stop(self, classification_stop):
        assert_is_type(classification_stop, None, numeric)
        self._parms["classification_stop"] = classification_stop


    @property
    def regression_stop(self):
        """float: Stopping criterion for regression error (MSE) on training data (-1 to disable). (Default: 0)"""
        return self._parms.get("regression_stop")

    @regression_stop.setter
    def regression_stop(self, regression_stop):
        assert_is_type(regression_stop, None, numeric)
        self._parms["regression_stop"] = regression_stop


    @property
    def stopping_rounds(self):
        """
        int: Early stopping based on convergence of stopping_metric. Stop if simple moving average of length k of the
        stopping_metric does not improve for k:=stopping_rounds scoring events (0 to disable) (Default: 5)
        """
        return self._parms.get("stopping_rounds")

    @stopping_rounds.setter
    def stopping_rounds(self, stopping_rounds):
        assert_is_type(stopping_rounds, None, int)
        self._parms["stopping_rounds"] = stopping_rounds


    @property
    def stopping_metric(self):
        """
        Enum["auto", "deviance", "logloss", "mse", "rmse", "mae", "rmsle", "auc", "lift_top_group", "misclassification",
        "mean_per_class_error"]: Metric to use for early stopping (AUTO: logloss for classification, deviance for
        regression) (Default: "auto")
        """
        return self._parms.get("stopping_metric")

    @stopping_metric.setter
    def stopping_metric(self, stopping_metric):
        assert_is_type(stopping_metric, None, Enum("auto", "deviance", "logloss", "mse", "rmse", "mae", "rmsle", "auc", "lift_top_group", "misclassification", "mean_per_class_error"))
        self._parms["stopping_metric"] = stopping_metric


    @property
    def stopping_tolerance(self):
        """
        float: Relative tolerance for metric-based stopping criterion (stop if relative improvement is not at least this
        much) (Default: 0)
        """
        return self._parms.get("stopping_tolerance")

    @stopping_tolerance.setter
    def stopping_tolerance(self, stopping_tolerance):
        assert_is_type(stopping_tolerance, None, numeric)
        self._parms["stopping_tolerance"] = stopping_tolerance


    @property
    def max_runtime_secs(self):
        """float: Maximum allowed runtime in seconds for model training. Use 0 to disable. (Default: 0)"""
        return self._parms.get("max_runtime_secs")

    @max_runtime_secs.setter
    def max_runtime_secs(self, max_runtime_secs):
        assert_is_type(max_runtime_secs, None, numeric)
        self._parms["max_runtime_secs"] = max_runtime_secs


    @property
    def ignore_const_cols(self):
        """bool: Ignore constant columns. (Default: True)"""
        return self._parms.get("ignore_const_cols")

    @ignore_const_cols.setter
    def ignore_const_cols(self, ignore_const_cols):
        assert_is_type(ignore_const_cols, None, bool)
        self._parms["ignore_const_cols"] = ignore_const_cols


    @property
    def shuffle_training_data(self):
        """bool: Enable global shuffling of training data. (Default: True)"""
        return self._parms.get("shuffle_training_data")

    @shuffle_training_data.setter
    def shuffle_training_data(self, shuffle_training_data):
        assert_is_type(shuffle_training_data, None, bool)
        self._parms["shuffle_training_data"] = shuffle_training_data


    @property
    def mini_batch_size(self):
        """
        int: Mini-batch size (smaller leads to better fit, larger can speed up and generalize better). (Default: 32)
        """
        return self._parms.get("mini_batch_size")

    @mini_batch_size.setter
    def mini_batch_size(self, mini_batch_size):
        assert_is_type(mini_batch_size, None, int)
        self._parms["mini_batch_size"] = mini_batch_size


    @property
    def clip_gradient(self):
        """float: Clip gradients once their absolute value is larger than this value. (Default: 10)"""
        return self._parms.get("clip_gradient")

    @clip_gradient.setter
    def clip_gradient(self, clip_gradient):
        assert_is_type(clip_gradient, None, numeric)
        self._parms["clip_gradient"] = clip_gradient


    @property
    def network(self):
        """
        Enum["auto", "user", "lenet", "alexnet", "vgg", "googlenet", "inception_bn", "resnet"]: Network architecture.
        (Default: "auto")
        """
        return self._parms.get("network")

    @network.setter
    def network(self, network):
        assert_is_type(network, None, Enum("auto", "user", "lenet", "alexnet", "vgg", "googlenet", "inception_bn", "resnet"))
        self._parms["network"] = network


    @property
    def backend(self):
        """Enum["auto", "mxnet", "caffe", "tensorflow"]: Deep Learning Backend. (Default: "mxnet")"""
        return self._parms.get("backend")

    @backend.setter
    def backend(self, backend):
        assert_is_type(backend, None, Enum("auto", "mxnet", "caffe", "tensorflow"))
        self._parms["backend"] = backend


    @property
    def image_shape(self):
        """List[int]: Width and height of image. (Default: [0, 0])"""
        return self._parms.get("image_shape")

    @image_shape.setter
    def image_shape(self, image_shape):
        assert_is_type(image_shape, None, [int])
        self._parms["image_shape"] = image_shape


    @property
    def channels(self):
        """int: Number of (color) channels. (Default: 3)"""
        return self._parms.get("channels")

    @channels.setter
    def channels(self, channels):
        assert_is_type(channels, None, int)
        self._parms["channels"] = channels


    @property
    def sparse(self):
        """bool: Sparse data handling (more efficient for data with lots of 0 values). (Default: False)"""
        return self._parms.get("sparse")

    @sparse.setter
    def sparse(self, sparse):
        assert_is_type(sparse, None, bool)
        self._parms["sparse"] = sparse


    @property
    def gpu(self):
        """bool: Whether to use a GPU (if available). (Default: True)"""
        return self._parms.get("gpu")

    @gpu.setter
    def gpu(self, gpu):
        assert_is_type(gpu, None, bool)
        self._parms["gpu"] = gpu


    @property
    def device_id(self):
        """List[int]: Device IDs (which GPUs to use). (Default: [0])"""
        return self._parms.get("device_id")

    @device_id.setter
    def device_id(self, device_id):
        assert_is_type(device_id, None, [int])
        self._parms["device_id"] = device_id


    @property
    def network_definition_file(self):
        """str: Path of file containing network definition (graph, architecture)."""
        return self._parms.get("network_definition_file")

    @network_definition_file.setter
    def network_definition_file(self, network_definition_file):
        assert_is_type(network_definition_file, None, str)
        self._parms["network_definition_file"] = network_definition_file


    @property
    def network_parameters_file(self):
        """str: Path of file containing network (initial) parameters (weights, biases)."""
        return self._parms.get("network_parameters_file")

    @network_parameters_file.setter
    def network_parameters_file(self, network_parameters_file):
        assert_is_type(network_parameters_file, None, str)
        self._parms["network_parameters_file"] = network_parameters_file


    @property
    def mean_image_file(self):
        """str: Path of file containing the mean image data for data normalization."""
        return self._parms.get("mean_image_file")

    @mean_image_file.setter
    def mean_image_file(self, mean_image_file):
        assert_is_type(mean_image_file, None, str)
        self._parms["mean_image_file"] = mean_image_file


    @property
    def export_native_parameters_prefix(self):
        """str: Path (prefix) where to export the native model parameters after every iteration."""
        return self._parms.get("export_native_parameters_prefix")

    @export_native_parameters_prefix.setter
    def export_native_parameters_prefix(self, export_native_parameters_prefix):
        assert_is_type(export_native_parameters_prefix, None, str)
        self._parms["export_native_parameters_prefix"] = export_native_parameters_prefix


    @property
    def activation(self):
        """
        Enum["rectifier", "tanh"]: Activation function. Only used if no user-defined network architecture file is
        provided, and only for problem_type=dataset.
        """
        return self._parms.get("activation")

    @activation.setter
    def activation(self, activation):
        assert_is_type(activation, None, Enum("rectifier", "tanh"))
        self._parms["activation"] = activation


    @property
    def hidden(self):
        """
        List[int]: Hidden layer sizes (e.g. [200, 200]). Only used if no user-defined network architecture file is
        provided, and only for problem_type=dataset.
        """
        return self._parms.get("hidden")

    @hidden.setter
    def hidden(self, hidden):
        assert_is_type(hidden, None, [int])
        self._parms["hidden"] = hidden


    @property
    def input_dropout_ratio(self):
        """float: Input layer dropout ratio (can improve generalization, try 0.1 or 0.2). (Default: 0)"""
        return self._parms.get("input_dropout_ratio")

    @input_dropout_ratio.setter
    def input_dropout_ratio(self, input_dropout_ratio):
        assert_is_type(input_dropout_ratio, None, numeric)
        self._parms["input_dropout_ratio"] = input_dropout_ratio


    @property
    def hidden_dropout_ratios(self):
        """
        List[float]: Hidden layer dropout ratios (can improve generalization), specify one value per hidden layer,
        defaults to 0.5.
        """
        return self._parms.get("hidden_dropout_ratios")

    @hidden_dropout_ratios.setter
    def hidden_dropout_ratios(self, hidden_dropout_ratios):
        assert_is_type(hidden_dropout_ratios, None, [numeric])
        self._parms["hidden_dropout_ratios"] = hidden_dropout_ratios


    @property
    def problem_type(self):
        """
        Enum["auto", "image", "text", "dataset"]: Problem type, auto-detected by default. If set to image, the H2OFrame
        must contain a string column containing the path (URI or URL) to the images in the first column. If set to text,
        the H2OFrame must contain a string column containing the text in the first column. If set to dataset, Deep Water
        behaves just like any other H2O Model and builds a model on the provided H2OFrame (non-String columns).
        (Default: "auto")
        """
        return self._parms.get("problem_type")

    @problem_type.setter
    def problem_type(self, problem_type):
        assert_is_type(problem_type, None, Enum("auto", "image", "text", "dataset"))
        self._parms["problem_type"] = problem_type



    # Ask the H2O server whether a Deep Water model can be built (depends on availability of native backends)
    @staticmethod
    def available():
        """
        Returns True if a deep water model can be built, or False otherwise.
        """
        builder_json = h2o.api("GET /3/ModelBuilders", data={"algo": "deepwater"})
        visibility = builder_json["model_builders"]["deepwater"]["visibility"]
        if (visibility == "Experimental"):
            print("Cannot build a Deep Water model - no backend found.")
            return False
        else:
            return True
